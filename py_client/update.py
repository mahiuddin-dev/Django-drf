import requests

endpoit = "http://127.0.0.1:8000/api/product/12/update/"

data = {
    'title': 'Hello I am a new title',
    'price': 500,
}

get_response = requests.put(endpoit, json=data) 

print(get_response.json())