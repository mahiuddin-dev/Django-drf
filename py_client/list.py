import requests

endpoit = "http://127.0.0.1:8000/api/product/"

get_response = requests.get(endpoit)

print(get_response.json())