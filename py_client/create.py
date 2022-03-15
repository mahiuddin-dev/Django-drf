import requests

endpoit = "http://127.0.0.1:8000/api/product/"

data = {
    'title': 'Everyday i want to be a better programmer',
}

get_response = requests.post(endpoit, json=data)

print(get_response.json())