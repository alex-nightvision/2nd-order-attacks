from flask import Flask, request, jsonify
import requests
import functions

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_user():
    return functions.hide_from_sast(request)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
