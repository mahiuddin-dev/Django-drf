import requests

# endpoit = "http://www.httpbin.org/status/200/"
# endpoit = "http://www.httpbin.org/anything"
endpoit = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoit,params={"product_id":123} ,json={"query":"hello World"}) # Get method

get_response = requests.post(endpoit ,json={"title":"Dinajpur", 'description':'django'}) # Get method



# print(get_response.headers)
print(get_response.json())

# print(get_response.text) # Print html code
# print(get_response.status_code) # Print status code
# print(get_response.json()["name"]) # Print json code

# Json is -> Javascript Object Notation != Python Dictionary
# REST Api HTTP request -> Json
# HTTP request -> HTML
# print(get_response.status_code) # Print status code
# print(get_response.json()) # Print json code


