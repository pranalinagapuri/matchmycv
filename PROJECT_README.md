# MatchMyCV 📄✨

**MatchMyCV** is a smart resume–job matching tool that helps recruiters quickly find the best resumes for a given job description.  
It parses resumes, stores them in a database, and ranks them against job postings using NLP + job market APIs.

---

## 🚀 Features

- 📤 Upload resumes (PDF/DOCX) via API
- 🗄️ Store resumes in a SQLite database
- 🔍 Search & rank resumes against a job description
- 🌐 Fetch live job descriptions using the Adzuna API
- ⚡ Built with **FastAPI** for blazing-fast performance
- 🧰 Easy setup with `requirements.txt`

---

## 🛠 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** SQLite + SQLAlchemy
- **NLP/Matching:** Python libraries (scikit-learn, etc.)
- **External API:** Adzuna Jobs API
- **Environment:** Virtualenv / venv

---

## 📂 Project Structure

```
backend/
│── app/
│   └── main.py          # FastAPI routes & resume matching logic
│── uploads/             # Resume upload folder
│── database.py          # SQLite + SQLAlchemy models
│── resumes.db           # SQLite database file
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── .gitignore           # Ignore env, db, uploads, etc.
```

---

## ⚙️ Setup Instructions (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/pranalinagapuri/matchmycv.git
   cd matchmycv/backend
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file** (inside `backend/`)
   ```bash
   ADZUNA_APP_ID=your_app_id
   ADZUNA_APP_KEY=your_app_key
   ```

5. **Run the app**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:8000/docs
   ```
   (Interactive Swagger UI 🚀)

---

## 🎯 Example Usage

- **Upload Resume:** `POST /upload/`  
- **Search Jobs:** `GET /search/?query=python+developer&location=uk`  
- **Match Resume to Job:** `POST /match/`

---

## 🔮 Next Steps (Future Improvements)

- 🌐 Frontend (React/Next.js) for recruiter-friendly UI  
- ☁️ Deploy backend to **Render / Railway / AWS**  
- 📊 Advanced ranking with embeddings / AI models  
- 👥 User authentication (Recruiter login)  

---

## 👩‍💻 Author

**Pranali Nagapuri**  
📌 Open to Software Engineering / Data roles  
🔗 [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com/pranalinagapuri)  

---

⭐ If you like this project, consider giving it a star on GitHub!
