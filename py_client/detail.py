import requests

endpoit = "http://127.0.0.1:8000/api/product/4/"

# get_response = requests.get(endpoit,params={"product_id":123} ,json={"query":"hello World"}) # Get method

get_response = requests.get(endpoit) # Get method

# print(get_response.headers)
print(get_response.json())