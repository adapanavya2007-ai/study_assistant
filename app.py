# # from flask import Flask, request, jsonify
# # import os
# # import requests
# # from dotenv import load_dotenv

# # load_dotenv()

# # app = Flask(__name__)

# # SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

# # headers = {
# #     "api-subscription-key": SARVAM_API_KEY,
# #     "Content-Type": "application/json"
# # }

# # @app.route("/")
# # def home():
# #     return "Sarvam API is running!"

# # @app.route("/translate", methods=["POST"])
# # def translate():
# #     data = request.get_json()
# #     text = data.get("text")
# #     source = data.get("source_language", "en-IN")
# #     target = data.get("target_language", "te-IN")

# #     url = "https://api.sarvam.ai/translate"
# #     payload = {
# #         "input": text,
# #         "source_language_code": source,
# #         "target_language_code": target,
# #         "model": "mayura:v1",
# #         "enable_preprocessing": True
# #     }

# #     response = requests.post(url, json=payload, headers=headers)
# #     result = response.json()

# #     return jsonify({"translated_text": result.get("translated_text", "Translation failed")})


# # @app.route("/tts", methods=["POST"])
# # def tts():
# #     data = request.get_json()
# #     text = data.get("text")
# #     language = data.get("language", "te-IN")

# #     url = "https://api.sarvam.ai/text-to-speech"
# #     payload = {
# #         "inputs": [text],
# #         "target_language_code": language,
# #         "speaker": "meera",
# #         "model": "bulbul:v1"
# #     }

# #     response = requests.post(url, json=payload, headers=headers)
# #     result = response.json()

# #     return jsonify({"audio": result.get("audios", [None])[0]})

# # @app.route("/stt", methods=["POST"])
# # def stt():
# #     file = request.files.get("file")
# #     language = request.form.get("language", "te-IN")

# #     url = "https://api.sarvam.ai/speech-to-text"
# #     files = {"file": (file.filename, file.stream, file.content_type)}
# #     stt_headers = {"api-subscription-key": SARVAM_API_KEY}

# #     response = requests.post(url, files=files, headers=stt_headers)
# #     result = response.json()

# #     return jsonify({"transcript": result.get("transcript", "Transcription failed")})


# # if __name__ == "__main__":
# #     app.run(debug=True, port=5001)
# from flask import Flask, request, jsonify
# import os
# import requests
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)

# # Get API key
# SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

# if not SARVAM_API_KEY:
#     raise ValueError("❌ SARVAM_API_KEY not found in .env file")

# # Common headers
# headers = {
#     "api-subscription-key": SARVAM_API_KEY,
#     "Content-Type": "application/json"
# }


# # ---------------- HOME ROUTE ----------------
# @app.route("/")
# def home():
#     return "✅ Sarvam AI Flask API is running!"


# # ---------------- TRANSLATE ----------------
# @app.route("/translate", methods=["POST"])
# def translate():
#     try:
#         data = request.get_json()

#         if not data:
#             return jsonify({"error": "JSON body required"}), 400

#         text = data.get("text")
#         source = data.get("source_language", "en-IN")
#         target = data.get("target_language", "te-IN")

#         if not text:
#             return jsonify({"error": "Text is required"}), 400

#         payload = {
#             "input": text,
#             "source_language_code": source,
#             "target_language_code": target,
#             "model": "mayura:v1",
#             "enable_preprocessing": True
#         }

#         response = requests.post(
#             "https://api.sarvam.ai/translate",
#             json=payload,
#             headers=headers
#         )

#         result = response.json()

#         return jsonify({
#             "translated_text": result.get("translated_text", "Translation failed")
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # ---------------- TEXT TO SPEECH ----------------
# @app.route("/tts", methods=["POST"])
# def tts():
#     try:
#         data = request.get_json()
#         text = data.get("text")

#         if not text:
#             return jsonify({"error": "Text required"}), 400

#         payload = {
#             "inputs": [text],
#             "target_language_code": data.get("language", "te-IN")
#         }

#         response = requests.post(
#             "https://api.sarvam.ai/text-to-speech",
#             json=payload,
#             headers=headers,
#             timeout=60
#         )

#         result = response.json()

#         if "audios" not in result:
#             return jsonify({
#                 "error": "No audio returned",
#                 "full_response": result
#             })

#         return jsonify({
#             "audio_base64": result["audios"][0]
#         })

#     except requests.exceptions.Timeout:
#         return jsonify({"error": "Sarvam API timeout"}), 504

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # ---------------- SPEECH TO TEXT ----------------
# @app.route("/stt", methods=["POST"])
# def stt():
#     try:
#         file = request.files.get("file")

#         if not file:
#             return jsonify({"error": "Audio file is required"}), 400

#         files = {
#             "file": (file.filename, file.stream, file.content_type)
#         }

#         response = requests.post(
#             "https://api.sarvam.ai/speech-to-text",
#             files=files,
#             headers={"api-subscription-key": SARVAM_API_KEY}
#         )

#         result = response.json()

#         return jsonify({
#             "transcript": result.get("transcript", "Transcription failed")
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # ---------------- RUN APP ----------------
# if __name__ == "__main__":
#     app.run(debug=True, port=5001)
from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API key
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

if not SARVAM_API_KEY:
    raise ValueError("SARVAM_API_KEY not found in .env file")

headers = {
    "api-subscription-key": SARVAM_API_KEY,
    "Content-Type": "application/json"
}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "Sarvam AI Flask API running successfully"


# ---------------- TRANSLATE ----------------
@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "JSON body required"}), 400

        text = data.get("text")
        source = data.get("source_language", "en-IN")
        target = data.get("target_language", "te-IN")

        payload = {
            "input": text,
            "source_language_code": source,
            "target_language_code": target,
            "model": "mayura:v1",
            "enable_preprocessing": True
        }

        response = requests.post(
            "https://api.sarvam.ai/translate",
            json=payload,
            headers=headers
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- TEXT TO SPEECH ----------------
@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json()
        text = data.get("text")

        payload = {
            "inputs": [text],
            "target_language_code": data.get("language", "te-IN")
        }

        response = requests.post(
            "https://api.sarvam.ai/text-to-speech",
            json=payload,
            headers=headers
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- SPEECH TO TEXT ----------------
# # ---------------- SPEECH TO TEXT (multiple files) ----------------
@app.route("/stt", methods=["POST"])
def stt():
    try:
        # Get all uploaded files with the same key 'file'
        files = request.files.getlist("file")

        if not files:
            return jsonify({"error": "Audio file(s) required"}), 400

        all_texts = []

        for f in files:
            # Send each file to Sarvam STT API
            response = requests.post(
                "https://api.sarvam.ai/speech-to-text",
                files={"file": (f.filename, f.stream, f.content_type)},
                headers={"api-subscription-key": SARVAM_API_KEY}
            )

            result = response.json()
            all_texts.append({f.filename: result})

        # Return transcriptions for all files
        return jsonify(all_texts)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)