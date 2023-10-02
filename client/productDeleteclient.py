import requests

product_id = input("What is the Product Id? \n")

try:
    product_id = int(product_id)
except:
    product_id= None
    print(f'{product_id} is not valid.') 

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    response = requests.delete(endpoint)
    print(response.status_code, response.status_code == 204)

