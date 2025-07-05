# 💼CarrerCraft (Job AI Assistant)

An intelligent desktop assistant that helps job seekers by leveraging the power of AI to enhance resumes, generate personalized cover letters, and offer career guidance — all through a user-friendly interface.

---

## 🚀 Features

- ✅ **Resume Upload:** Upload your resume in `.pdf` or `.docx` format.
- 🧠 **AI-Powered Assistance:** Uses OpenAI GPT models to analyze, enhance, and generate resume suggestions.
- 📝 **Cover Letter Generation:** Generate personalized cover letters for job roles using AI.
- 📄 **Save as PDF:** Save the AI-generated content directly as a PDF.
- 💬 **Chat Interface:** Ask career-related questions and get smart responses.
- 🖥️ **Simple & Clean Interface:** Built using Python (Tkinter/Streamlit/Flask) with minimalistic design.
- 🔐 **Environment Variables:** Securely manage API keys using `.env`.

---

## 🧰 Tech Stack

| Component       | Technology        |
|----------------|-------------------|
| Backend Logic  | Python 3.10+       |
| AI Engine      | OpenAI GPT-4 / GPT-3.5 |
| UI Framework   | Tkinter / Streamlit / Flask |
| File Handling  | Python `os`, `docx`, `PyMuPDF` |
| PDF Export     | `reportlab` / `fpdf` / `pdfkit` |
| Environment    | `python-dotenv`    |

---

## 📂 Project Structure

job_ai_assistant/
│
├── main.py # Main application logic
├── ui/ # UI modules (Tkinter or Streamlit)
├── core/ # AI and processing logic
│ ├── resume_parser.py
│ ├── ai_suggester.py
│ └── pdf_exporter.py
├── assets/ # Icons, logos, styles
├── .env # Stores OpenAI API key
├── requirements.txt # Python dependencies
└── README.md # You're here!

