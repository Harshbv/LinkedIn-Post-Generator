# LinkedIn Post Generator

An AI-powered tool that helps you create LinkedIn posts in a **natural, human-like writing style**.

You give it a topic (and optionally **tone, length, language, and target audience**), and it generates a polished LinkedIn post for you.

This is useful for:

- Students who want to post about projects, internships, or achievements  
- Professionals who want to stay active on LinkedIn without spending 30+ minutes per post  
- Creators/influencers who want consistent, on-brand content quickly  

---

## ✨ Features

- 🧠 AI-generated posts that mimic real LinkedIn writing style  
- 🎯 Control over **topic, language, and length** (Short / Medium / Long)  
- 🎭 Control over **tone** (Professional, Casual, Motivational, Funny)  
- 👥 Optional **target audience** field to tailor the post  
  - e.g. “fresh graduates”, “hiring managers”, “Gen Z devs”  
- 📚 Uses **few-shot examples + a dataset of real posts** for more realistic output  
- 🌐 Modern **Streamlit web UI** with a dark / orange theme  
- 📋 Copy-friendly output (code block) + **Download as `.txt`** for quick posting  
- 🔐 Uses a local **`.env`** file to keep your API key safe (not committed to GitHub)  

---

## 🏗 Project Structure

```text
LinkedIn-Post-Generator/
├─ data/
│  ├─ raw_posts.json          # Original example posts
│  └─ processed_posts.json    # Cleaned/processed posts used for generation
├─ few_shot.py                # Few-shot helper: loads posts, tags, and examples
├─ llm_helper.py              # Helper functions to call the Groq LLM via LangChain
├─ post_generator.py          # Core logic to build prompts and generate the final LinkedIn post
├─ preprocess.py              # Preprocessing scripts for the dataset
├─ main.py                    # Streamlit app entry point (UI)
├─ requirements.txt           # Python dependencies
├─ .gitignore                 # Files and folders ignored by Git
└─ .env                       # ⚠️ NOT in Git – stores your API key locally
```
⚙️ Setup
1. Clone the repository
 ```text
git clone https://github.com/Harshbv/LinkedIn-Post-Generator.git
cd LinkedIn-Post-Generator
```
2. Create and activate a virtual environment (recommended)
```text
python -m venv .venv
```
Windows:
```text
.venv\Scripts\activate
```

macOS / Linux:
```text
source .venv/bin/activate
```
3. Install dependencies
```text
pip install -r requirements.txt
```
🔑 Environment Variables

Create a file named .env in the project root (same folder as main.py) and add your API key:
```text
GROQ_API_KEY=your_api_key_here
```
🚀 How to Run

From the project root:
```text
streamlit run main.py
```

This will:

  Start a local Streamlit server

  Open the app in your browser (usually at http://localhost:8501)

In the UI, you can:

  Select a Title/Tag (e.g. “Job Search”, “Work Life Balance”, “Gen Z”)

  Choose Length: Short / Medium / Long

  Choose Language: English / Hinglish

  Choose Tone: Professional / Casual / Motivational / Funny

  (Optionally) enter a Target audience, e.g.

   “fresh graduates”

   “mid-level data scientists”

  “hiring managers in SaaS”

  Then click Generate.

The app will:

  Build a structured prompt based on your inputs

  Pull a few few-shot examples from processed_posts.json that match the tag

  Call the LLM via llm_helper.py

  Generate a LinkedIn-style post and display it in:

  A normal text section

  A copy-friendly code block

A downloadable .txt file
