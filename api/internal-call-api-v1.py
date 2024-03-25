import requests
requests.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/requests')

#from flask import Flask, jsonify

#app = Flask(__name__)

#@app.route('/api/response', methods=['GET'])

#def get_data():
   # url = "https://malydevops.pl"
    
   # response = requests.get(url)
   # response_json = response.json()
   # print(response_json)
    #return jsonify(response_json)

#if __name__ == '__main__':
 #   app.run(debug=True)

url = "https://malydevops.pl"
response = requests.get(url)
print(response.status_code)