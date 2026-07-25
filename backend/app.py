from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all domains and routes
CORS(app, resources={r"/*": {"origins": "*"}})

# 1. LEADS DATASET
leads_db = [
    {
        "id": 1,
        "name": "Sheikh Mansoor",
        "email": "mansoor@dubailuxury.ae",
        "budget": "$15,000,000",
        "timeline": "30 Days",
        "region": "UAE",
        "score": "HOT LEAD 🔥",
        "desk": "VIP Desk (Dubai)"
    },
    {
        "id": 2,
        "name": "Alexander Vance",
        "email": "+1 (305) 892-1102",
        "budget": "$4,500,000",
        "timeline": "Immediate",
        "region": "USA",
        "score": "WARM LEAD 🟡",
        "desk": "Sarah Jenkins"
    },
    {
        "id": 3,
        "name": "Nguyen Minh",
        "email": "minh.nguyen@saigonprop.vn",
        "budget": "$2,800,000",
        "timeline": "60 Days",
        "region": "Vietnam",
        "score": "HOT LEAD 🔥",
        "desk": "Tran Le"
    }
]

# 2. SAFETY & SOS DATASET
agents_safety_db = [
    {"id": 101, "agent": "Sarah Jenkins", "location": "Miami Beach Penthouse #402", "status": "Active Showing", "battery": "88%", "sos_alert": False},
    {"id": 102, "agent": "Tran Le", "location": "Saigon Center Tower B", "status": "En Route", "battery": "94%", "sos_alert": False},
    {"id": 103, "agent": "Vikram Malhotra", "location": "Worli Sea Face Villa", "status": "Active Showing", "battery": "42%", "sos_alert": False}
]

# 3. RERA & LEGAL AUDIT DATASET
legal_audit_db = [
    {"id": 501, "property": "Worli Sea Face Villa", "rera_id": "PRM/KA/RERA/1251/2024", "jurisdiction": "India (MahaRERA)", "status": "CLEAR ✅", "risk_score": "LOW (2%)"},
    {"id": 502, "property": "Miami Beach Penthouse", "rera_id": "US-FL-DISC-9921", "jurisdiction": "USA (Florida Title)", "status": "CLEAR ✅", "risk_score": "LOW (1%)"},
    {"id": 503, "property": "Downtown Dubai Tower 4", "rera_id": "DLD-RERA-88391", "jurisdiction": "UAE (RERA Dubai)", "status": "PENDING REVIEW ⚠️", "risk_score": "MED (18%)"}
]

def calculate_ai_score(budget_num, timeline):
    if budget_num >= 5000000 or "Immediate" in timeline or "30" in timeline:
        return "HOT LEAD 🔥", "VIP Desk Auto-Assigned"
    elif budget_num >= 1000000:
        return "WARM LEAD 🟡", "Standard Sales Desk"
    else:
        return "NURTURE LEAD 🔵", "Automated Email Sequences"

@app.route('/')
def home():
    return jsonify({"status": "Aetheris AI Backend is Active & Ready!"})

# LEADS ENDPOINTS
@app.route('/api/leads', methods=['GET'])
def get_leads():
    total_val = sum([int(str(l['budget']).replace('$', '').replace(',', '')) for l in leads_db])
    return jsonify({
        "success": True,
        "total_pipeline": total_val,
        "leads": leads_db
    })

@app.route('/api/leads', methods=['POST'])
def create_lead():
    data = request.json or {}
    name = data.get('name', 'Anonymous Lead')
    contact = data.get('contact', 'N/A')
    budget_raw = data.get('budget', '0')
    timeline = data.get('timeline', '30 Days')
    region = data.get('region', 'Global')

    try:
        budget_num = int(str(budget_raw).replace('$', '').replace(',', ''))
    except ValueError:
        budget_num = 1000000

    score, desk = calculate_ai_score(budget_num, timeline)

    new_lead = {
        "id": len(leads_db) + 1,
        "name": name,
        "email": contact,
        "budget": f"${budget_num:,}",
        "timeline": timeline,
        "region": region,
        "score": score,
        "desk": desk
    }
    leads_db.insert(0, new_lead)
    return jsonify({"success": True, "lead": new_lead}), 201

# SAFETY & SOS ENDPOINTS
@app.route('/api/safety', methods=['GET'])
def get_safety_status():
    active_alerts = len([a for a in agents_safety_db if a['sos_alert']])
    return jsonify({
        "success": True,
        "active_alerts": active_alerts,
        "agents": agents_safety_db
    })

@app.route('/api/safety/sos', methods=['POST'])
def trigger_sos():
    data = request.json or {}
    agent_id = data.get('agent_id', 101)
    
    for agent in agents_safety_db:
        if agent['id'] == agent_id:
            agent['sos_alert'] = True
            agent['status'] = "🚨 EMERGENCY SOS TRIGGERED"
            return jsonify({"success": True, "message": f"EMERGENCY DISPATCH TRIGGERED FOR {agent['agent']}", "agent": agent}), 200
            
    return jsonify({"success": False, "message": "Agent not found"}), 404

# RERA & LEGAL AUDIT ENDPOINTS
@app.route('/api/legal', methods=['GET'])
def get_legal_status():
    verified_count = len([item for item in legal_audit_db if "CLEAR" in item['status']])
    return jsonify({
        "success": True,
        "verified_count": verified_count,
        "audits": legal_audit_db
    })

@app.route('/api/legal/verify', methods=['POST'])
def run_legal_audit():
    data = request.json or {}
    prop_name = data.get('property', 'New Luxury Listing')
    jur = data.get('jurisdiction', 'Global RERA')
    
    new_audit = {
        "id": 500 + len(legal_audit_db) + 1,
        "property": prop_name,
        "rera_id": f"RERA-AUTO-{len(legal_audit_db)+100}",
        "jurisdiction": jur,
        "status": "CLEAR ✅",
        "risk_score": "LOW (0%)"
    }
    legal_audit_db.insert(0, new_audit)
    return jsonify({"success": True, "audit": new_audit}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



   
  


