from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_user():
    name = request.args.get('name')
    print(name)
    if not name:
        return {"error": "Name parameter is required"}

    url = f"http://127.0.0.1:5000/users?name={name}"
    response = requests.get(url).json()
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
