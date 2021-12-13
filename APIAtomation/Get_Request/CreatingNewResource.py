import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users'

# Read input json file
file = open('C:\\Users\\galst\\Documents\\גל סטרוביניץ\\json-api.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body

response = requests.post(url, request_json)
print(response.content)

# Validating Response code
assert response.status_code == 201

# Fetch header from response

print(response.headers.get('Content-Length'))

# Parse response to json format
response_json = json.loads(response.text)
print(response_json)

# Pick ID using Json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])