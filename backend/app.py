import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connection

# Initialize OpenAI client (Set your OPENAI_API_KEY environment variable)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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
        data = request.json
        user_messages = data.get("messages", [])

        # Inject system prompt at the start
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + user_messages

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
