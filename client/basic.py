import requests

endpoint = "http://localhost:8000/api/postdata/"

response =  requests.post(endpoint, json = {"name": "Randsauce1",
                                            "age": 21,"faculty": "SOC",
                                            "department": "CSS",
                                            "description": "170IQ"})
try:
    data = response.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Error: Invalid JSON response")
