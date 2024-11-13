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
tenant_ids = ["ca.alameda","ca.albany","ca.berkeley","ca.dublin","ca.emeryville","ca.fremont","ca.hayward","ca.livermore","ca.newark","ca.oakland","ca.piedmont","ca.pleasanton","ca.sanleandro","ca.unioncity","ca.losangeles","ca.longbeach","ca.glendale","ca.santaclarita","ca.lancaster","ca.palmdale","ca.pomona","ca.torrance","ca.pasadena","ca.elmonte","ca.downey","ca.inglewood","ca.westcovina","ca.norwalk","ca.anaheim","ca.brea","ca.buenapark","ca.costamesa","ca.cypress","ca.danapoint","ca.fountainvalley","ca.fullerton","ca.gardengrove","ca.huntingtonbeach","ca.irvine","ca.lagunabeach","ca.lagunaniguel","ca.sandiego","ca.carlsbad","ca.chulavista","ca.coronado","ca.delmar","ca.elcajon","ca.encinitas","ca.escondido","ca.imperialbeach","ca.lamesa","ca.lemongrove","ca.nationalcity","ca.oceanside","ca.poway","ca.sanjose","ca.cupertino","ca.gilroy","ca.losaltos","ca.losgatos","ca.milpitas","ca.montesereno","ca.morganhill","ca.mountainview","ca.paloalto","ca.santaclara","ca.saratoga","ca.sunnyvale","ca.sacramento","ca.citrusheights","ca.elkgrove","ca.folsom","ca.galt","ca.isleton","ca.ranchocordova"]  # Add all tenant IDs here

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
                    "tenantId": "ca"
                }
            ],
            "active": True,
            "tenantId": "ca",
            "permanentCity": None
        }
    },
    "billingSlab": [
        {
            "tenantId": "",
            "licenseType": "PERMANENT",
            "applicationType": "RENEWAL",
            "structureType": "IMMOVABLE.PUCCA",
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
            "applicationType": "RENEWAL",
            "structureType": "IMMOVABLE.PUCCA",
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
            "applicationType": "RENEWAL",
            "structureType": "IMMOVABLE.PUCCA",
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
            "applicationType": "RENEWAL",
            "structureType": "IMMOVABLE.PUCCA",
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
            "applicationType": "RENEWAL",
            "structureType": "IMMOVABLE.PUCCA",
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
    # Create a new payload for each tenant to avoid modifying the original
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