from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://router.huggingface.co/hf-inference/v1/chat/completions"
API_KEY = os.getenv("HF_API_KEY")   # ❗ API key is NOT written here

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

if __name__ == "__main__":
    app.run()
