
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "Você é um mastologista online, ético, empático, sem diagnósticos."},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"reply": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(debug=True)
