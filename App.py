from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Hidden internal server and token
TARGET_URL = "http://198.99.157.68:3724/api/import/Purchase-Order-Details"
AUTH_TOKEN = "699c4c2c-e17f-4850-afd6-bc185ca84708"

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "text/csv"
    }

    try:
        response = requests.post(TARGET_URL, headers=headers, data=file.stream)
        return jsonify({"status": response.status_code, "response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
