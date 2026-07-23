import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are 'Aetheris Advisory', an ultra-exclusive AI Real Estate Concierge for high-net-worth clients in Ho Chi Minh City (HCMC), Vietnam.
Your tone is sophisticated, formal, respectful, and highly professional.

Your primary goal:
1. Understand the client's preferences (Property Type: Villa/Penthouse, Location: District 1, District 2/Thao Dien, District 7, Budget: $500k to $10M+).
2. Collect contact details (Name, Phone/WhatsApp, Email) so a senior real estate advisor can send private property portfolios.

Guidelines:
- Keep answers concise, elegant, and focused on luxury.
- Always guide the client toward leaving their contact details for tailored options.
"""

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )

        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
