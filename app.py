
1791898220098_image.png
give me this text and i will copy and another place we copy

Here is the text from the image, ready to copy:

I want to create an app which user will upload a resume and the app will tell the ATS score and the improvements in the resume. I will use streamlit for UI. I will use gemini flash model for AI models. Give me two files app.py, readme file and requirments.txt and make sure to review and test it before you give me code. Also tell me how to push on github using UI and deploy it on streamlit.
I copied it exactly as written, including the small typos (“requirments.txt”). If you’d like, I can also give you a cleaned-up version with the spelling fixed, and I can build the app for you right here.

I want to create an app which user will upload a resume and the app will tell the ATS score and the improvements in the resume. I will use streamlit for UI. I will use gemini flash model for AI models. Give me two files app.py, readme file and requirments.txt and make sure to review and test it before you give me code. Also tell me how to push on github using UI and deploy it on streamlit.

Building a Streamlit app under offline constraints.
Building a Streamlit app under offline constraints.
I’ll build it, then test it before handing it over. First, let me check what’s available in my environment.

Ran 4 commands, created a file, shared files
I’ve built your app and tested it. I also added a small .gitignore that keeps your API key out of GitHub.

What it does
The user uploads a PDF or DOCX resume.
Gemini Flash returns an ATS score out of 100, a score for each of five categories, strengths, weaknesses and prioritized improvements.
It also lists missing keywords, and you can paste a job description to score the match against it.
The API key comes from Streamlit secrets, an environment variable, or the sidebar box.
What I tested
I ran 36 checks and all of them passed:

Resume reading: real PDF and DOCX files, including resumes laid out in tables, plus corrupt files, scanned/blank PDFs and wrong file types.
Gemini replies: clean JSON, JSON with extra text around it, empty replies and badly formatted replies.
Scores: out-of-range or wrong-type values are handled, so the page never crashes.
Page flow: the happy path, a missing API key, a failed Gemini call, an oversized file and the idle state.
Limitation: I had no internet here, so I could not install Streamlit or call the real Gemini API. I tested the app’s logic on real files with stand-ins for those two. Before you share it, run it once with your own key and a real resume.

Push to GitHub using the website
Sign in at github.com and click + → New repository.
Name it (for example ats-resume-checker), choose Public (the free Streamlit Cloud tier needs a public repo), and click Create repository.
On the empty repo page, click uploading an existing file.
Drag in app.py, requirements.txt, README.md and .gitignore. Add .gitignore too if your file manager hides it.
Write a commit message such as “Initial commit” and click Commit changes.
Never upload a file containing your API key.

Deploy on Streamlit Community Cloud
Go to share.streamlit.io and sign in with GitHub, allowing access to your repo.
Click Create app and choose Deploy a public app from GitHub.
Select your repository, branch main, and main file path app.py.
Click Advanced settings → Secrets and paste GEMINI_API_KEY = "your-key-here". You can get a free key at aistudio.google.com/apikey.
Click Deploy and wait a few minutes. You’ll get a public link to share.
The default model is gemini-2.5-flash, and the sidebar lets you type a newer Flash model name if Google has released one.


App
PY 

Requirements
TXT 

Readme
Document·MD 

.gitignore
GITIGNORE 




Claude is AI and can make mistakes. Please double-check responses.
Claude finished the response
a
