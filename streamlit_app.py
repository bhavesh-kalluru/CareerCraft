import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader

# Load .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Job Assistant", layout="centered")
st.title("🧠 AI Job Assistant")

# Upload or paste
uploaded_file = st.file_uploader("📄 Upload Resume or Job Description", type=["pdf", "txt"])
jd_text = ""

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        jd_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    else:
        jd_text = uploaded_file.read().decode("utf-8")

else:
    jd_text = st.text_area("Or Paste Job Description Here:", height=200)

# Task selection
task = st.selectbox("Select Task", [
    "Tailor Resume",
    "Write Cover Letter",
    "Predict Interview Questions",
    "Hard Interview Questions",
    "Medium Interview Questions",
    "Beginner Interview Questions",
    "HR Interview Questions"
])

def generate(prompt):
    try:
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career coach who helps with resumes, cover letters, and interview prep."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.7
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

if st.button("🚀 Generate"):
    if not jd_text:
        st.warning("⚠️ Please upload or paste job description.")
    else:
        prompt_map = {
            "Tailor Resume": f"Rewrite resume bullet points tailored to this job:\n{jd_text}",
            "Write Cover Letter": f"Write a professional cover letter:\n{jd_text}",
            "Predict Interview Questions": f"List 5 common interview questions:\n{jd_text}",
            "Hard Interview Questions": f"List 5 hard technical questions:\n{jd_text}",
            "Medium Interview Questions": f"List 5 medium-level questions:\n{jd_text}",
            "Beginner Interview Questions": f"List 5 beginner-friendly interview questions:\n{jd_text}",
            "HR Interview Questions": f"List 5 common HR questions:\n{jd_text}",
        }

        output = generate(prompt_map[task])
        st.subheader("📄 Output")
        st.text_area("", output, height=250)




