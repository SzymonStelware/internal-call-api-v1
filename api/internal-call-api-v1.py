import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/response', methods=['GET'])

def get_data():
    url = "https://malydevops.pl"
    
    response = requests.get(url)
    response_json = response.json()
    return jsonify(print(response_json))
    #return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True, port=1234)