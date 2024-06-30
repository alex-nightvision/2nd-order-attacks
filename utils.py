import requests

def get_name(request):
    return request.args.get('name')

def fetch_user_data(name):
    url = f"http://127.0.0.1:5000/users?name={name}"
    response = requests.get(url).json()
    return response
