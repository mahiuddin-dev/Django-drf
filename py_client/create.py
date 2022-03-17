import requests

endpoit = "http://127.0.0.1:8000/api/product/"

headers = {'Authorization': 'Bearer 99733e1e1f63d12e0fa14bb983bd84b0454a98ac'}

data = {
    'title': 'Everyday i want to be a better programmer',
}

get_response = requests.post(endpoit, json=data, headers=headers)

print(get_response.json())