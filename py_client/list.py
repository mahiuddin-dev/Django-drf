import requests
from getpass import getpass

auth_endpoit = "http://127.0.0.1:8000/api/auth/"


username = input('Enter username: ')
password = getpass('Enter password: ')

data = {
    'username': username,
    'password': password
}

auth_response = requests.post(auth_endpoit, json=data)

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    # headers = {'Authorization': f'Token {token}'}
    headers = {'Authorization': f'Bearer {token}'}

    endpoit = "http://127.0.0.1:8000/api/product/"

    get_response = requests.get(endpoit, headers=headers)

    print(get_response.json())