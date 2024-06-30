from flask import Flask, request, jsonify
import requests

def hide_from_sast(request):
    name = request.args.get('name')

    # # shows Server-Side Request Forgery (SSRF) but this is not SQL Injection
    # url = f"http://127.0.0.1:5000/users?name={name}"

    # Hard coded not show up in semgrep at all
    if "foo" in name:
        url = f"http://127.0.0.1:5000/users?name=foobar"
    else:
        url = "http://127.0.0.1:5000/users?name='%20OR%20'1'='1"

    # make request
    response = requests.get(url).json()
    return response
