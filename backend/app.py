from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Module 5 Revenue Data
revenue_db = [
    {"forecast_rev": "$120,000", "broker_split": "$36,000", "agent_split": "$84,000"},
    {"forecast_rev": "$85,000", "broker_split": "$25,500", "agent_split": "$59,500"},
    {"forecast_rev": "$210,000", "broker_split": "$63,000", "agent_split": "$147,000"}
]

@app.route('/')
def home():
    return jsonify({"status": "Aetheris AI Solutions Backend is Running!"})

@app.route('/revenue', methods=['GET'])
def get_revenue_analytics():
    return jsonify({"success": True, "analytics": revenue_db})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
