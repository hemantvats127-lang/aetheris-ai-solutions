# 5. MODULE 5: EXECUTIVE REVENUE & DEAL ANALYTICS DATASET
revenue_db = [
    {"id": 801, "region": "UAE 🇦🇪", "forecast_rev": "$1,200,000", "broker_split": "70%", "agent_split": "30%", "deals_closed": 12},
    {"id": 802, "region": "USA 🇺🇸", "forecast_rev": "$850,000", "broker_split": "60%", "agent_split": "40%", "deals_closed": 8},
    {"id": 803, "region": "India 🇮🇳", "forecast_rev": "$600,000", "broker_split": "75%", "agent_split": "25%", "deals_closed": 15},
    {"id": 804, "region": "Vietnam 🇻🇳", "forecast_rev": "$450,000", "broker_split": "65%", "agent_split": "35%", "deals_closed": 9}
]

# 6. MODULE 6: ESCROW & DEAL ROOM STATUS DATASET
escrow_db = [
    {"id": 901, "property": "Downtown Dubai Tower 4", "token_amt": "$150,000", "escrow_status": "FUNDED 🔒", "doc_sign": "Signed ✍️", "closing_date": "2026-08-15"},
    {"id": 902, "property": "Miami Beach Penthouse", "token_amt": "$45,000", "escrow_status": "PENDING ⏳", "doc_sign": "In Review 📄", "closing_date": "2026-08-30"},
    {"id": 903, "property": "Worli Sea Face Villa", "token_amt": "$80,000", "escrow_status": "FUNDED 🔒", "doc_sign": "Signed ✍️", "closing_date": "2026-09-05"}
]

# MODULE 5 ENDPOINT
@app.route('/revenue', methods=['GET'])
def get_revenue_analytics():
    return jsonify({"success": True, "analytics": revenue_db})

# MODULE 6 ENDPOINT
@app.route('/escrow', methods=['GET'])
def get_escrow_status():
    funded_count = len([item for item in escrow_db if "FUNDED" in item['escrow_status']])
    return jsonify({
        "success": True,
        "funded_deals": funded_count,
        "deals": escrow_db
    })
