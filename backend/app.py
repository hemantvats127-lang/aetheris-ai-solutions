from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cross-Origin support for GitHub Pages frontend

# Sample initial leads dataset
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

def calculate_ai_score(budget_num, timeline):
    """Simple AI heuristic scoring engine logic"""
    if budget_num >= 5000000 or "Immediate" in timeline or "30" in timeline:
        return "HOT LEAD 🔥", "VIP Desk Auto-Assigned"
    elif budget_num >= 1000000:
        return "WARM LEAD 🟡", "Standard Sales Desk"
    else:
        return "NURTURE LEAD 🔵", "Automated Email Sequences"

@app.route('/')
def home():
    return jsonify({"status": "Aetheris AI Backend is Active & Ready!"})

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
    leads_db.insert(0, new_lead) # Top par add karo

    return jsonify({"success": True, "lead": new_lead}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



