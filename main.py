from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://router.huggingface.co/hf-inference/v1/chat/completions"
API_KEY = os.getenv("HF_API_KEY")  # Environment variable (do not put key here)


# Home route (important)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "running", "message": "Mays AI is live!"})


# Chat API route
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/Llama-3.2-3B-Instruct",
        "messages": [
            {"role": "user", "content": user_msg}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    return jsonify(response.json())


# Run app on Render server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
