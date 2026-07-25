from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy / Initial Database for Module 5 & Module 6
revenue_db = [
    {"forecast_rev": "$120,000", "broker_split": "$36,000", "agent_split": "$84,000"},
    {"forecast_rev": "$85,000", "broker_split": "$25,500", "agent_split": "$59,500"}
]

escrow_db = [
    {"token_amt": "$5,000", "doc_sign": "Verified", "escrow_status": "FUNDED"},
    {"token_amt": "$2,500", "doc_sign": "Pending", "escrow_status": "PENDING"}
]

@app.route('/')
def home():
    return jsonify({"status": "Aetheris AI Solutions Backend is Running!"})

@app.route('/revenue', methods=['GET'])
def get_revenue_analytics():
    return jsonify({"success": True, "analytics": revenue_db})

@app.route('/escrow', methods=['GET'])
def get_escrow_status():
    funded_count = len([item for item in escrow_db if "FUNDED" in item['escrow_status']])
    return jsonify({
        "success": True,
        "funded_deals": funded_count,
        "deals": escrow_db
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
