@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json or {}
        user_message = data.get('message', '')

        # Simple & Guaranteed Lead Detection
        has_email = "@" in user_message
        has_phone = any(char.isdigit() for char in user_message) and len(user_message) >= 8

        if has_email or has_phone:
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

            trigger_crm_automation(lead_entry)
            captured_leads.append(lead_entry)

        # AI Reply Logic (Tumhara existing Groq/Llama call)
        # ai_reply = ... 

        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("Error in /chat:", e)  # Render logs me error dikhega
        return jsonify({"reply": "I apologize, our VIP server connection is refreshing. How may I assist your query?"}), 500
