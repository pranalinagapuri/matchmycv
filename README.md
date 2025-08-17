# MatchMyCV

This project lets you upload a resume, parse skills, and match with job postings from the Adzuna API.

---

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/pranalinagapuri/matchmycv.git
cd matchmycv/backend
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Copy the example file:
```bash
cp .env.example .env
```

Then edit `.env` with your real keys:
```
ADZUNA_APP_ID=your_real_app_id
ADZUNA_APP_KEY=your_real_app_key
```

### 5. Run the app
```bash
uvicorn app.main:app --reload
```

Then open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📂 Project Structure
```
├── app/
│   └── main.py
├── uploads/
│   └── sample_cv.pdf
├── requirements.txt
├── database.py
├── resumes.db
├── .env.example
└── README.md
```

---

## 🔧 Tech Stack
- **FastAPI** (Python backend)  
- **SQLite** (database)  
- **Adzuna API** (job search)  
- **Pydantic & SQLAlchemy** (validation & ORM)  

---

## ✨ Features
- Upload Resume → parses skills  
- Search Job → fetches Adzuna jobs  
- Match → calculates similarity score  
