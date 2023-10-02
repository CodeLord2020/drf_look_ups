import requests
from getpass import getpass

username = input("What is your username (lowercase): ")
auth_endpoint = "http://localhost:8000/api/token/"
password = getpass()

auth_response = requests.post(auth_endpoint, json={"username":username, "password":password})
try: 
    data = auth_response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Error: Invalid JSON response")


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers ={
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    data = {'name': 'iphone 4 (Silver)',
            'category': 'artifact', 'price': 12000.0,
            'discount': False}

    p_response = requests.post(endpoint, headers=headers, json=data)

    try:
        p_data = p_response.json()
        print(p_data)  
    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid JSON response") 