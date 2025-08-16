from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
import fitz  # PyMuPDF
from docx import Document

# --------------------------
# Database setup
# --------------------------
DATABASE_URL = "sqlite:///./resumes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(Text)

Base.metadata.create_all(bind=engine)

# --------------------------
# FastAPI setup
# --------------------------
app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------
# Endpoints
# --------------------------

# 1. Upload CV
@app.post("/upload-cv", tags=["Resumes"])
async def upload_cv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Extract text
    extracted_text = ""
    if file.filename.endswith(".pdf"):
        doc = fitz.open(file_location)
        for page in doc:
            extracted_text += page.get_text()
    elif file.filename.endswith(".docx"):
        doc = Document(file_location)
        extracted_text = "\n".join([p.text for p in doc.paragraphs])

    resume = Resume(filename=file.filename, content=extracted_text)
    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {"id": resume.id, "filename": resume.filename, "status": "uploaded"}

# 2. List Resumes
@app.get("/resumes", tags=["Resumes"])
def list_resumes(db: Session = Depends(get_db)):
    resumes = db.query(Resume).all()
    return [{"id": r.id, "filename": r.filename, "snippet": r.content[:200]} for r in resumes]

# 3. Search Resumes
@app.get("/search", tags=["Resumes"])
def search_resumes(q: str, db: Session = Depends(get_db)):
    results = db.query(Resume).filter(Resume.content.contains(q)).all()
    return [{"id": r.id, "filename": r.filename, "snippet": r.content[:200]} for r in results]

# 4. View Resume by ID
@app.get("/resume/{resume_id}", tags=["Resumes"])
def get_resume(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        return {"error": "Resume not found"}
    return {"id": resume.id, "filename": resume.filename, "content": resume.content}

# 5. Delete Resume
@app.delete("/delete/{resume_id}", tags=["Resumes"])
def delete_resume(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        return {"status": "error", "id": resume_id}
    db.delete(resume)
    db.commit()
    return {"status": "deleted", "id": resume_id}
