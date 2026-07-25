from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allows frontend to make requests from GitHub Pages

# Sample database for Module 1 (Lead Gen)
MOCK_LEADS = [
    {"id": 1, "company": "VinHomes Luxury Realty", "email": "contact@vinhomes-luxury.vn", "phone": "+84 90 123 4567", "status": "Verified", "niche": "Real Estate"},
    {"id": 2, "company": "Saigon Premier Properties", "email": "info@saigonpremier.com", "phone": "+84 91 876 5432", "status": "Verified", "niche": "Real Estate"},
    {"id": 3, "company": "HCMC Elite Estates", "email": "sales@hcmcelite.vn", "phone": "+84 93 333 2211", "status": "Pending", "niche": "Real Estate"},
    {"id": 4, "company": "Metropole Thu Thiem Agent", "email": "leads@metropole-thuthiem.vn", "phone": "+84 98 444 5566", "status": "Verified", "niche": "Real Estate"}
]

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "system": "Aetheris AI Solutions Backend", "version": "1.0"})

# MODULE 1 API: Scraping / Fetching Leads
@app.route('/api/module1/scrape', methods=['POST'])
def scrape_leads():
    data = request.get_json() or {}
    niche = data.get("niche", "Luxury Real Estate")
    location = data.get("location", "Ho Chi Minh City")
    limit = int(data.get("limit", 10))

    # Return filtered/scraped mock results
    results = MOCK_LEADS[:limit]
    return jsonify({
        "success": True,
        "niche": niche,
        "location": location,
        "total_scraped": len(results),
        "leads": results
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
