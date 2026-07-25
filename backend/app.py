import os
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Real-time In-Memory Database for Aetheris REOS
captured_leads = [
    {
        "id": 1,
        "name": "Sheikh Mansoor",
        "contact": "mansoor@dubailuxury.ae",
        "budget": "$15,000,000",
        "timeline": "30 Days",
        "score": "HOT LEAD 🔥",
        "assigned_agent": "VIP Desk (Dubai)",
        "location": "UAE",
        "timestamp": "2026-07-25 09:30:00"
    },
    {
        "id": 2,
        "name": "Alexander Vance",
        "contact": "+1 (305) 892-1102",
        "budget": "$4,500,000",
        "timeline": "Immediate",
        "score": "WARM LEAD 🟡",
        "assigned_agent": "Sarah Jenkins",
        "location": "USA",
        "timestamp": "2026-07-25 10:05:00"
    },
    {
        "id": 3,
        "name": "Nguyen Minh",
        "contact": "minh.nguyen@saigonprop.vn",
        "budget": "$2,800,000",
        "timeline": "60 Days",
        "score": "HOT LEAD 🔥",
        "assigned_agent": "Tran Le",
        "location": "Vietnam",
        "timestamp": "2026-07-25 10:12:00"
    }
]

agent_safety_logs = []

def sanitize_input(user_text):
    if not isinstance(user_text, str):
        return ""
    forbidden = ["ignore previous", "system prompt", "jailbreak", "override"]
    clean_text = user_text
    for word in forbidden:
        clean_text = clean_text.replace(word, "[BLOCKED_INJECTION]")
    return clean_text

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "Aetheris AI Solutions Backend Active",
        "version": "2026.1",
        "regions": ["USA", "UAE", "Vietnam"]
    })

# 1. VIP Chat Endpoint with Security Guardrails & Lead Detection
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        raw_message = data.get('message', '')
        user_message = sanitize_input(raw_message)

        if "[BLOCKED_INJECTION]" in user_message:
            return jsonify({
                "reply": "I am Alexander, VIP Concierge for Aetheris AI Solutions. I can only assist with verified real estate inquiries."
            })

        # Lead Auto-Detection (Email or Phone check)
        has_email = "@" in user_message
        has_phone = any(char.isdigit() for char in user_message) and len(user_message) >= 8

        if has_email or has_phone:
            is_high_value = any(word in user_message.lower() for word in ["penthouse", "villa", "3m", "4m", "5m", "buy", "visit"])
            score = "HOT LEAD 🔥" if is_high_value else "WARM LEAD 🟡"
            
            new_lead = {
                "id": len(captured_leads) + 1,
                "name": "Incoming VIP Lead",
                "contact": user_message,
                "budget": "$3,000,000+",
                "timeline": "Qualified via Chat",
                "score": score,
                "assigned_agent": "Senior VIP Concierge",
                "location": "Global",
                "timestamp": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            }
            captured_leads.append(new_lead)

        ai_reply = f"Thank you for reaching out to Aetheris AI Solutions. Our VIP concierge team has logged your query: '{user_message}'"
        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("Error in /chat:", e)
        return jsonify({"reply": "System refreshing. Please try again."}), 500

# 2. Owner Dashboard API (Aetheris Owner Suite Data)
@app.route('/api/admin/leads', methods=['GET'])
def get_owner_leads():
    total_val = 22300000
    return jsonify({
        "system": "Aetheris AI Solutions Owner Suite",
        "pipeline_value_usd": f"${total_val:,}",
        "total_qualified_leads": len(captured_leads),
        "active_showings": 4,
        "leads": captured_leads
    })

# 3. Field Agent Physical Safety Emergency SOS Endpoint
@app.route('/api/sos', methods=['POST'])
def trigger_sos():
    try:
        data = request.get_json(silent=True) or {}
        agent_name = data.get('agent_name', 'Field Agent')
        location = data.get('location', 'Unknown Site')
        lat = data.get('latitude', '0.0')
        lng = data.get('longitude', '0.0')

        sos_entry = {
            "event": "PHYSICAL_SAFETY_EMERGENCY",
            "agent": agent_name,
            "location": location,
            "maps_url": f"https://www.google.com/maps?q={lat},{lng}",
            "timestamp": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
        agent_safety_logs.append(sos_entry)

        print("🚨 EMERGENCY SOS DISPATCHED:", sos_entry)
        return jsonify({"status": "EMERGENCY_DISPATCHED", "details": sos_entry})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 



