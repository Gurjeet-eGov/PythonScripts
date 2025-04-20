import requests
import json
import time

# Endpoint URL
url = "http://localhost:8082/tl-calculator/billingslab/_create"  # Replace with your actual endpoint

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# List of tenant IDs
tenant_ids = ["ke.nairobi","ke.mombasa","ke.kisumu","ke.nakuru","ke.uasin gishu"]  # Add all tenant IDs here

# Base request payload
base_payload = {
    "RequestInfo": {
        "authToken": "a4c35063-6a87-4671-a63b-8b92de760a4f",
        "userInfo": {
            "id": 9421,
            "uuid": "3709110a-4b1d-49a4-b639-95b689a86aa5",
            "userName": "SUPERSU1",
            "name": "Jason",
            "mobileNumber": "9999009900",
            "emailId": None,
            "locale": None,
            "type": "EMPLOYEE",
            "roles": [
                {
                    "name": "Super User",
                    "code": "SUPERUSER",
                    "tenantId": "ke"
                }
            ],
            "active": True,
            "tenantId": "ke",
            "permanentCity": None
        }
    },
    "billingSlab": [
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": None,
    "accessoryCategory": "ACC-1",
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "200"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": None,
    "accessoryCategory": "ACC-2",
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "200"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": None,
    "accessoryCategory": "ACC-3",
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "200"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": None,
    "accessoryCategory": "ACC-4",
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "200"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": None,
    "accessoryCategory": "ACC-5",
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "200"
  }
]
}

# Loop through each tenant ID and send the POST request
for tenant_id in tenant_ids:
    # Create a NEW payload for each tenant to avoid modifying the original
    payload = base_payload.copy()
    
    # Update the tenantId for each billing slab entry
    for slab in payload["billingSlab"]:
        slab["tenantId"] = tenant_id
    # Send POST request
    try:
        response = requests.post(url, headers=headers, json=payload)
        # Print response for each request
        if response.status_code == 200:
            print(f"Successfully processed tenant ID: {tenant_id}")
        else:
            print(f"Failed to process tenant ID: {tenant_id}")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred for tenant ID: {tenant_id}")
        print(e)
    
    # Wait for 1 second before making the next request
    time.sleep(2)  # Adjust the wait time as needed