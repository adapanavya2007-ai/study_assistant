##📚 StudyAssistant

A simple AI-powered Study Assistant built using Flask that helps students understand study material easily using translation, text-to-speech, and speech-to-text features powered by Sarvam AI APIs.

**GitHub Repository:**
https://github.com/adapanavya2007-ai/studyassistant


---

##🚀 Features

🌍 Text Translation (Convert text from one language to another)

🔊 Text to Speech Conversion

🎤 Speech to Text Conversion

⚡ AI powered processing using Sarvam AI

🌐 REST API endpoints for AI services

📚 Helpful for students to learn in their native language



---

##🛠 Tech Stack

Python

Flask

Sarvam AI API

Requests

Python-dotenv



---

##▶ How to Run

**1️⃣ Create Virtual Environment**

python -m venv venv

Activate it (Windows):

venv\Scripts\activate


---

**2️⃣ Install Dependencies**

pip install -r requirements.txt


---

**3️⃣ Add Environment Variables**

Create a .env file in the project folder and add your Sarvam API key.

SARVAM_API_KEY=your_api_key_here


---

**4️⃣ Run the Application**

python app.py


---

**5️⃣ Open in Browser**

http://127.0.0.1:5001/


---

##📁 Project Structure

StudyAssistant/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md


---

**🌐 API Endpoints**

Home

GET /

Returns server status.


---

Translate Text

POST /translate

Used to translate text from one language to another.

Parameters:

text – text to translate
source_language – source language code
target_language – target language code


---

Text to Speech

POST /tts

Converts text input into speech audio in the selected language.

Parameter:

text – text to convert into speech
language – target language code


---

Speech to Text

POST /stt

Uploads audio files and converts spoken speech into text.

Parameter:

file – audio file(s) containing speech


---

##🌍 Push Project to GitHub

1️⃣ Initialize Git

git init

2️⃣ Add Files

git add .

3️⃣ Commit

git commit -m "Initial commit"

4️⃣ Create Repository on GitHub
Go to https://github.com
Click New Repository
Copy the repository URL

5️⃣ Connect Local Project to GitHub

git remote add origin https://github.com/adapanavya2007-ai/study_assistant.git

6️⃣ Push to GitHub

git branch -M main
git push -u origin main


---

##👩‍💻 Author

Adapa Navya 


---

##⭐ Future Improvements

Add web interface for students

Support multiple language translation

Upload PDF and translate study material

Generate AI based study notes

Mobile application integration
