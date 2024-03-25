import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check-status', methods=['GET'])
def check_status():
    url = "https://malydevops.pl"
    
    try:
        response = requests.get(url)
        return jsonify({"url": url, "status_code": response.status_code})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/data', methods=['GET'])
def api_data():
    data = {"name": "Szymek", "age": 28}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=1234)