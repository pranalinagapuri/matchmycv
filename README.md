# MatchMyCV 🎯
An AI-powered resume–job matcher built with **FastAPI + SQLite + Adzuna Jobs API**.

Recruiters can:
- Upload candidate resumes (PDF/DOCX)
- Search live job postings
- Automatically compare resume skills with job descriptions
- Get a similarity score to speed up shortlisting

---

## 🚀 Features
- Resume parsing (text extraction from PDF/DOCX)
- Job search integration with [Adzuna API](https://developer.adzuna.com/)
- Cosine similarity scoring between resumes & job descriptions
- FastAPI backend with interactive **Swagger UI**
- SQLite database for storing resumes

---

## 📂 Project Structure
```bash
backend/
│── app/
│   ├── main.py          # FastAPI endpoints
│   ├── database.py      # SQLite database setup
│── uploads/             # Uploaded resumes
│── requirements.txt     # Python dependencies
│── resumes.db           # SQLite DB
│── .gitignore           # Ignored files
```

---

## ⚙️ Setup Instructions

### 1. Clone repo
```bash
git clone https://github.com/pranalinagapuri/matchmycv.git
cd matchmycv/backend
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API keys
Create a `.env` file in `backend/` with:
```ini
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_api_key
```

### 5. Run the app
```bash
uvicorn app.main:app --reload
```

Then open:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📸 Screenshots

- **Upload Resume** → parses skills
- **Search Job** → fetches Adzuna jobs
- **Match** → similarity score

---

## 🛠 Tech Stack
- **FastAPI** (Python backend)
- **SQLite** (database)
- **Adzuna API** (job search)
- **Pydantic & SQLAlchemy** (data validation & ORM)

---

## 📌 Next Steps (Optional)
- Build a React/HTML frontend for recruiters
- Deploy backend to Render/Railway/Heroku
- Add more NLP (spacy, transformers) for better parsing
