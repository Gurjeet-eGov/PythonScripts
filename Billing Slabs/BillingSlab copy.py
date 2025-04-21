import requests
import json
import time
import copy  # To properly copy nested structures

# Endpoint URL
url = "http://localhost:8082/tl-calculator/billingslab/_create"  # Replace with your actual endpoint

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# List of tenant IDs
tenant_ids = ["ke.nairobi", "ke.mombasa", "ke.kisumu", "ke.nakuru", "ke.uasin gishu"]  # Removed space issue
application_types = ["NEW", "RENEWAL"]
license_types = ["TEMPORARY"]
structure_types = ["IMMOVABLE.PUCCA", "IMMOVABLE.KUTCHA", "MOVABLE.HDV", "MOVABLE.MDV"]

# Directly defining the billing slab template
billing_slab_template = [
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
    "billingSlab": []
}

# Loop through each tenant and send the POST request
for tenant_id in tenant_ids:
    # Create a deep copy of base payload to avoid modifying original data
    payload = copy.deepcopy(base_payload)

    # Generate billing slabs dynamically
    billing_slabs = []
    for slab in billing_slab_template:
        for app_type in application_types:
            for lic_type in license_types:
                for struct_type in structure_types:
                    modified_slab = copy.deepcopy(slab)
                    modified_slab["tenantId"] = tenant_id
                    modified_slab["applicationType"] = app_type
                    modified_slab["licenseType"] = lic_type
                    modified_slab["structureType"] = struct_type
                    billing_slabs.append(modified_slab)

    # Assign updated billing slabs
    payload["billingSlab"] = billing_slabs

    # Send POST request
    try:
        response = requests.post(url, headers=headers, json=payload)

        # Print response
        if response.status_code == 200:
            print(f"✅ Successfully processed tenant: {tenant_id}")
        else:
            print(f"❌ Failed for tenant: {tenant_id}")
            print(f"Status Code: {response.status_code}")
            # print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error for tenant {tenant_id}: {e}")

    # Wait before next request
    time.sleep(5)  # Adjust time if needed
