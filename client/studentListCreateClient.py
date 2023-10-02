import requests
from getpass import getpass

username = input("What is your username (lowercase): ")
password = getpass()

auth_endpoint = "http://localhost:8000/api/token/"
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
    endpoint = "http://localhost:8000/api/"

    response = requests.get(endpoint, headers=headers)
    

    try: 
        data = response.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid JSON response")