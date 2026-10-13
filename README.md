# 📄 ATS Resume Checker

A Streamlit app that scores your resume for Applicant Tracking System (ATS) compatibility and gives specific improvement suggestions, powered by Google's Gemini Flash model.

## Features
- Upload a resume as **PDF** or **DOCX**
- Overall **ATS score (0-100)** with a category breakdown
- Strengths, weaknesses, and **prioritized improvements**
- Missing keywords
- Optional: paste a **job description** to score your match against it

## Run locally

1. Install Python 3.10+.
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Get a free Gemini API key at https://aistudio.google.com/apikey
4. Provide the key (choose one):
   - Paste it into the app's sidebar, **or**
   - Set an environment variable: `GEMINI_API_KEY`, **or**
   - Create `.streamlit/secrets.toml` containing:
```toml
     GEMINI_API_KEY = "your-key"
```
5. Start the app:
```bash
   streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push this project to a GitHub repository.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app**, choose your repo, branch `main`, and main file `app.py`.
4. Open **Advanced settings → Secrets** and add:
```toml
   GEMINI_API_KEY = "your-key"
```
5. Click **Deploy**.

> Never commit your API key to GitHub. Use Streamlit secrets or the sidebar input.

## Project structure
```
app.py            # Streamlit app
requirements.txt  # Python dependencies
README.md         # This file
```

## Notes
- Scanned/image-only PDFs can't be read; use a text-based PDF or DOCX.
- The score is an AI estimate, not the result of a real employer's ATS.
