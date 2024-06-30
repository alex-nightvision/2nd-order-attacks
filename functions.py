from flask import Flask, request, jsonify
import requests

def hide_from_sast(request):
    # # shows Server-Side Request Forgery (SSRF) but this is not SQL Injection
    # name = request.args.get('name')
    # url = f"http://127.0.0.1:5000/users?name={name}"

    # Hard coded not show up in semgrep at all
    url = "http://127.0.0.1:5000/users?name='%20OR%20'1'='1"

    # make request
    response = requests.get(url).json()
    return response
