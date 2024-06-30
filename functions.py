from flask import Flask, request, jsonify
import requests

def hide_from_sast(request):
    name = request.args.get('name')
    url = f"http://127.0.0.1:5000/users?name={name}"
    response = requests.get(url).json()
    return response
