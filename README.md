# LinkedIn Post Generator

An AI-powered tool that helps you create LinkedIn posts in a natural, human-like writing style.  
You give it a topic (and optionally tone, length, and language), and it generates a polished LinkedIn post for you.

This is useful for:
- Students who want to post about projects, internships, or achievements  
- Professionals who want to stay active on LinkedIn without spending 30+ minutes per post  
- Creators/influencers who want consistent, on-brand content quickly  

---

## ✨ Features

- 🧠 AI-generated posts that mimic human writing style  
- 🎯 Control over topic, language, and length (short/medium/long)  
- 📚 Uses few-shot examples + a dataset of real posts for better, more realistic output  
- 🔐 Uses a local `.env` file to keep your API key safe (not committed to GitHub)  

---

## 🏗 Project Structure

```text
LinkedIn-Post-Generator/
├─ data/
│  ├─ raw_posts.json          # Original example posts
│  └─ processed_posts.json    # Cleaned/processed posts used for generation
├─ few_shot.py                # Few-shot examples / prompt templates
├─ llm_helper.py              # Helper functions to call the LLM (Groq)
├─ post_generator.py          # Core logic to build the final LinkedIn post
├─ preprocess.py              # Preprocessing scripts for the dataset
├─ main.py                    # Entry point to run the generator
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

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
🔑 Environment variables
Create a file named .env in the project root (same folder as main.py) and add your API key:

text
Copy code
GROQ_API_KEY=your_api_key_here
⚠️ Never commit .env to GitHub. It’s already added to .gitignore so it stays local and secret.

🚀 How to Run
From the project root:

bash
Copy code
python main.py
The script will typically:

Ask you for:

Topic (e.g. “my first internship”, “learning Python”, “hackathon experience”)

Desired length (short / medium / long)

Language (e.g. English, Hindi, etc. if supported)

Call the LLM using the helper in llm_helper.py

Generate a LinkedIn-style post based on your inputs plus the examples in data/ and few_shot.py

Print the final post to the console for you to copy to LinkedIn

🧪 Customization
You can tweak the behavior by editing:

few_shot.py

Change or add few-shot examples to adjust style and tone.

data/raw_posts.json & data/processed_posts.json

Add your own LinkedIn posts to better match your voice.

post_generator.py

Adjust temperature, max tokens, or formatting of the final output.
