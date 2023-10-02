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


student_id = input("What is the Student Id? \n")

try:
    student_id = int(student_id)
    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        headers ={
            "Authorization": f"Bearer {token}"
        }
        if student_id:
            endpoint = f"http://localhost:8000/api/getdata/{student_id}/"
            response = requests.get(endpoint, headers=headers)
        try: 
            data = response.json()
            print(data)
        except requests.exceptions.JSONDecodeError:
            print("Error: Invalid JSON response")

except:
    student_id= None
    print(f'{student_id} is not valid id.') 
