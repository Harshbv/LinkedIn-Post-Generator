# LinkedIn Post Generator

An AI-powered tool that helps you create LinkedIn posts in a **natural, human-like writing style**.

You give it a topic (and optionally tone, length, language, and target audience), and it generates a polished LinkedIn post for you.

This is useful for:

- Students who want to post about projects, internships, or achievements  
- Professionals who want to stay active on LinkedIn without spending 30+ minutes per post  
- Creators/influencers who want consistent, on-brand content quickly  

---

## ✨ Features

- 🧠 AI-generated posts that mimic real LinkedIn writing style  
- 🎯 Control over **topic, language, and length** (short / medium / long)  
- 🎭 Control over **tone** (Professional, Casual, Motivational, Funny)  
- 👥 Optional **target audience** field to tailor the post (e.g. “fresh graduates”, “hiring managers”, “Gen Z devs”)  
- 📚 Uses few-shot examples + a dataset of real posts for more realistic output  
- 🌐 Modern **Streamlit web UI** with a dark / orange theme  
- 📋 Copy-friendly output (code block) + **Download as `.txt`** for quick posting  
- 🔐 Uses a local `.env` file to keep your API key safe (not committed to GitHub)  

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
⚙️ Setup
1. Clone the repository
bash
Copy code
git clone https://github.com/Harshbv/LinkedIn-Post-Generator.git
cd LinkedIn-Post-Generator
2. Create and activate a virtual environment (recommended)
bash
Copy code
python -m venv .venv
Windows:

bash
Copy code
.venv\Scripts\activate
macOS / Linux:

bash
Copy code
source .venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
🔑 Environment Variables
Create a file named .env in the project root (same folder as main.py) and add your API key:

env
Copy code
GROQ_API_KEY=your_api_key_here
⚠️ Never commit .env to GitHub.
It’s already added to .gitignore so it stays local and secret.

🚀 How to Run
From the project root:

bash
Copy code
streamlit run main.py
This will:

Start a local Streamlit server

Open the app in your browser (usually at http://localhost:8501)

In the UI, you can:

Select a Title/Tag (e.g. “Job Search”, “Work Life Balance”, “Gen Z”)

Choose Length: Short / Medium / Long

Choose Language: English / Hinglish

Choose Tone: Professional / Casual / Motivational / Funny

(Optionally) enter a Target audience:

e.g. “fresh graduates”, “mid-level data scientists”, “hiring managers in SaaS”

Then click Generate.

The app will:

Build a structured prompt based on your inputs

Pull a few few-shot examples from processed_posts.json that match the tag

Call the LLM via llm_helper.py

Generate a LinkedIn-style post and display it in:

A normal text section

A copy-friendly code block

A downloadable .txt file

🧪 Customization
You can tweak the behavior by editing:

few_shot.py
Change how examples are selected (e.g. filter by length/language or just tag)

Extend tags or logic if you add more data to processed_posts.json

data/raw_posts.json & data/processed_posts.json
Add your own LinkedIn posts to better match your writing style

Run preprocess.py to:

Extract line counts

Detect language (English / Hinglish)

Normalize tags

post_generator.py
Adjust:

Prompt wording

How tone and target audience are used

Number of few-shot examples included

Add extra controls (e.g. temperature, max tokens) if desired

main.py
Tweak the UI layout and styling (Streamlit + custom CSS)

Change available tones, tags, defaults, or colors

🛠 Technologies Used
Python – Core language used to build the app

Streamlit – Frontend UI for interacting with the generator

LangChain & langchain_groq – For structuring prompts and talking to the Groq LLM

Groq LLM API – Backend large language model that generates LinkedIn-style posts

pandas – For loading and transforming the example post datasets in data/

python-dotenv – To securely load GROQ_API_KEY from a local .env file

JSON datasets – To store and reuse real/processed LinkedIn posts for better style control
