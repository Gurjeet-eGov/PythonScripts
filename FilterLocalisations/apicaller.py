import json
import requests

# Endpoint URL
url = "http://localhost:8082/localization/messages/v1/_upsert"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Load grouped results from the JSON file
with open("grouped_results.json", "r") as file:
    grouped_results = json.load(file)

# Request info template
request_info = {
    "apiId": "mgramseva",
    "ver": ".01",
    "ts": "",
    "action": "_create",
    "did": "1",
    "key": "",
    "msgId": "20170310130900|en_IN",
    "authToken": "a4c35063-6a87-4671-a63b-8b92de760a4f",
    "userInfo": {"id":9421,"uuid":"3709110a-4b1d-49a4-b639-95b689a86aa5",
                 "userName":"SUPERSU1", "name":"Jason","mobileNumber":"9999009900",
                 "emailId":None,"locale":None,"type":"EMPLOYEE",
                 "roles":[{"name":"Super User","code":"SUPERUSER","tenantId":"ca"}],
                 "active":True,"tenantId":"ca","permanentCity":None}
}

# Tenant ID
tenant_id = "ca"

# Iterate over each module in grouped results and send a request
for module, messages in grouped_results.items():
    # Prepare the request body
    payload = {
        "RequestInfo": request_info,
        "tenantId": tenant_id,
        "messages": messages
    }

    # Send POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check response status
    if response.status_code == 200:
        print(f"Successfully uploaded messages for module: {module}")
    else:
        print(f"Failed to upload messages for module: {module}")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
