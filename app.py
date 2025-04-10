from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")

        if not user_message:
            return jsonify({"error": "Campo 'message' é obrigatório no corpo da requisição."}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "Você é um mastologista online, ético, empático, sem diagnósticos."},
                {"role": "user", "content": user_message},
            ]
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
    print(f"Erro ocorrido: {str(e)}")  # Mostra o erro real no log da Render
    return jsonify({"error": "Erro interno no servidor."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
