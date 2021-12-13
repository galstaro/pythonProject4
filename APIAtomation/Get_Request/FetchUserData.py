import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send Get Request
response = requests.get(url)

# Display Response Content
print(response.content)
# print(response.headers)

# Parse respnose to Json FORMAT
json_response = json.loads(response.text)
print(json_response)

# Fetch value string Json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 2

for i in range(3):
    first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print(first_name[0])
