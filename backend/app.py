import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

PROPERTY_KNOWLEDGE_BASE = """
AETHERIS REAL ESTATE PORTFOLIO 2026 (HCMC):
1. The River Thủ Thiêm: Luxury 3BR Penthouse | $2.5M USD (~63.5 Billion VND) | 240 sqm | River View, Private Pool.
2. Serenade Villa District 2 (Thảo Điền): Private Compound | $4.8M USD (~122 Billion VND) | 600 sqm | 5 Bed, Garden.
3. Grand Marina Saigon (District 1): Executive Apartment | $1.2M USD (~30.5 Billion VND) | 110 sqm | High Floor.

CAPABILITIES:
- Instant USD to VND Currency Conversion.
- Direct Site Visit & Helicopter Transfer Booking.
"""

SYSTEM_PROMPT = f"""
You are Aetheris Private Advisory, an ultra-luxury AI Real Estate Concierge in Ho Chi Minh City.
Catalog:
{PROPERTY_KNOWLEDGE_BASE}

GOALS:
1. Provide instant property info and handle currency inquiries (USD/VND).
2. Capture full booking details (Name, Phone, Preferred Visit Date).
3. Always maintain a 5-star VIP concierge tone.
"""

captured_leads = []

def trigger_crm_automation(lead_data):
    """
    AUTOMATION ENGINE: 
    Simulates automated dispatch to CRM / Webhooks (e.g., Salesforce, HubSpot, or WhatsApp API).
    """
    print(f"[AUTOMATION TRIGGERED] Lead dispatched to CRM: {lead_data['assigned_agent']}")
    return True

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )
        ai_reply = response.choices[0].message.content

        # AUTOMATED LEAD EXTRACTION & SCORING
        has_email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', user_message)
        has_phone = re.search(r'\+?\d[\d -]{7,}\d', user_message)
        
        if has_email or has_phone:
            # Automation Logic: Intent & High-Value Lead Detection
            is_high_value = any(word in user_message.lower() for word in ["penthouse", "villa", "3m", "4m", "buy", "visit", "tomorrow"])
            score = "HOT LEAD 🔥" if is_high_value else "WARM LEAD 🟡"
            assigned_agent = "Senior Director (VIP Desk)" if score == "HOT LEAD 🔥" else "Standard Desk Agent"

            lead_entry = {
                "contact": user_message,
                "score": score,
                "assigned_agent": assigned_agent,
                "automation_status": "Auto-Dispatched to CRM & WhatsApp Webhook",
                "timestamp": "Real-time Sync"
            }
            
            # Run Automation
            trigger_crm_automation(lead_entry)
            captured_leads.append(lead_entry)

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": "I apologize, our VIP server connection is refreshing. How may I assist your query?"}), 500

@app.route('/api/admin/leads', methods=['GET'])
def get_leads():
    return jsonify({
        "status": "2026 CRM Sync Active",
        "total_leads": len(captured_leads), 
        "leads": captured_leads
    })
