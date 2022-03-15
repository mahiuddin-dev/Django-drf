import requests


product_id = input("Enter product id: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print("Invalid product id")

if product_id:
    endpoit = f"http://127.0.0.1:8000/api/product/{product_id}/delete/"
    get_response = requests.delete(endpoit) 
    print(get_response.status_code,get_response.status_code == 204)

    