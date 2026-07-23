from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Aetheris Advisory, an ultra-exclusive luxury real estate concierge in Ho Chi Minh City (HCMC).
Your tone is sophisticated, polite, and highly professional. You assist high-net-worth clients with acquiring villas, penthouses, and luxury estates."""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    bot_reply = completion.choices[0].message.content
    
    # Teeno common keys bhej rahe hain taaki frontend jo bhi demand kare, reply mil jaye
    return jsonify({
        "reply": bot_reply,
        "response": bot_reply,
        "message": bot_reply
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
