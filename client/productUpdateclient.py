import requests

product_id = input("What is the Product Id? \n")

try:
    product_id = int(product_id)
except:
    product_id= None
    print(f'{product_id} is not valid.') 

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/update/"

    data = {'name': 'iphone 14',
            'category': 'Mobile', 'price': 1300.0,
            'discount': True}

    response = requests.put(endpoint, json=data)

    try:
        data = response.json()
        print(data)    
    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid JSON response")