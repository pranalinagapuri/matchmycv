# 📄 MatchMyCV

MatchMyCV is a FastAPI-based web service that allows you to **upload, store, search, and manage resumes** easily.

🚀 Deployed and live at:  
👉 [https://matchmycv.onrender.com](https://matchmycv.onrender.com)

---

## 🌐 API Documentation

- **Swagger UI (Interactive API Testing):**  
  [https://matchmycv.onrender.com/docs](https://matchmycv.onrender.com/docs)

- **ReDoc (API Reference):**  
  [https://matchmycv.onrender.com/redoc](https://matchmycv.onrender.com/redoc)

---

## ⚡ Features

- 📤 Upload CVs (`POST /upload-cv`)
- 📋 List all CVs (`GET /resumes`)
- 🔍 Search resumes (`GET /search`)
- 🆔 Get resume by ID (`GET /resume/{resume_id}`)
- ❌ Delete resume (`DELETE /delete/{resume_id}`)

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** SQLite (via SQLAlchemy)
- **Deployment:** Render

---

## 🚀 Local Development

If you want to run this project locally:

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/matchmycv.git
   cd matchmycv
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI app**
   ```bash
   uvicorn app.main:app --reload
   ```

   Your app will now be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Project Structure

```
matchmycv/
│── app/                # Main FastAPI application
│── uploads/            # Uploaded resumes
│── database.py         # Database setup
│── requirements.txt    # Python dependencies
│── resumes.db          # SQLite database
│── README.md           # Project documentation
```

---

## 📜 License

This project is licensed under the MIT License.
