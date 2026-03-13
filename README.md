# 🎓 Study Assistant API

A simple **Study Assistant API** built using **Flask** and **Sarvam AI** that provides language and voice features such as **Translation, Text-to-Speech, and Speech-to-Text**.

---

## 🚀 Features

* 🌍 Translate Text Between Languages
* 🔊 Text to Speech Conversion
* 🎤 Speech to Text Conversion
* 🔐 Secure API Key using `.env`
* 🌐 REST API Endpoints
* 💻 Simple Flask Backend

---

## 🛠 Tech Stack

* Python
* Flask
* Sarvam AI API
* Requests
* python-dotenv

---

## ▶ How to Run

### 1️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate it (Windows):

```
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

OR

```
pip install flask requests python-dotenv
```

---

### 3️⃣ Create `.env` File

Create a `.env` file and add your **Sarvam API key**

```
SARVAM_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5001/
```

---

## 📁 Project Structure

```
Study-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🌍 API Endpoints

### Home

```
GET /
```

Returns API status.

---

### Translate Text

```
POST /translate
```

Example JSON

```
{
"text": "Hello",
"source_language": "en-IN",
"target_language": "te-IN"
}
```

---

### Text to Speech

```
POST /tts
```

Example JSON

```
{
"text": "Hello world",
"language": "te-IN"
}
```

---

### Speech to Text

```
POST /stt
```

Upload audio file(s) using **form-data**.

---

## 🌍 Push Project to GitHub

1️⃣ Initialize Git

```
git init
```

2️⃣ Add Files

```
git add .
```

3️⃣ Commit

```
git commit -m "Study Assistant API"
```

4️⃣ Create Repository on GitHub
Go to [https://github.com](https://github.com)
Click **New Repository**
Copy the repository URL

5️⃣ Connect Local Project to GitHub

```
git remote add origin https://github.com/your-username/study-assistant.git
```

6️⃣ Push to GitHub

```
git branch -M main
git push -u origin main
```

---

## 👩‍💻 Author

A. Navya

---

## ⭐ Future Improvements

* AI Chat Study Assistant
* PDF Question Answering
* Voice-based Learning Assistant
* Web UI Interface

---
