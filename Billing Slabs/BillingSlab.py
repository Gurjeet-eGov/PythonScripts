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
applicationType = ["NEW", "RENEWAL"]
licenseType = ["PERMANENT", "TEMPORARY"]
structureType = ["IMMOVABLE.PUCCA","IMMOVABLE.KUTCHA","MOVABLE.HDV","MOVABLE.MDV"]

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
    "tradeType": "GOODS.AUTOMOTIVE.AUTOPARTSRETAIL",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.CONSUMER ELECTRONICS.LAPTOPSANDCOMPUTERS",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.CONSUMER ELECTRONICS.MOBILEPHONES",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.FOOD & BEVERAGE.BEVERAGEPRODUCTION",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.FOOD & BEVERAGE.PACKAGEDFOODPRODUCTS",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.HEALTHCARE.DENTALLABSERVICES",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.HOME APPLIANCES.KITCHENAPPLIANCES",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.HOME APPLIANCES.LAUNDRYAPPLIANCES",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.HOME IMPROVEMENT.BUILDINGMATERIALS",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.RETAIL.CLOTHINGRETAIL",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.RETAIL.ELECTRONICSRETAIL",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.RETAIL.FURNITURERETAIL",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.RETAIL.GROCERYSTORE",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.SPORTING GOODS.FITNESSEQUIPMENT",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "GOODS.SPORTING GOODS.OUTDOOREQUIPMENT",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.CONSTRUCTION.DRYWALLINSTALLATION",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.CONSTRUCTION.PAINTING",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.ENVIRONMENTAL SERVICES.WASTEMANAGEMENT",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.FOOD SERVICE.CATERING",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.FOOD SERVICE.RESTAURANTMANAGEMENT",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.HVAC.HVACINSTALLATION",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.HVAC.HVACMAINTENANCE",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.INFORMATION TECHNOLOGY.ITSUPPORTSERVICES",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.INFORMATION TECHNOLOGY.SOFTWAREDEVELOPMENT",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.LANDSCAPING.LANDSCAPEDESIGN",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.LANDSCAPING.LAWNCAREANDMAINTENANCE",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.PERSONAL CARE.BARBERING",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.PERSONAL CARE.HAIRCUTTINGANDSTYLING",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
  },
  {
    "tenantId": "",
    "licenseType": "PERMANENT",
    "applicationType": "NEW",
    "structureType": "MOVABLE.MDV",
    "tradeType": "SERVICES.QUALITY CONTROL.INSPECTION",
    "accessoryCategory": None,
    "type": "FLAT",
    "uom": "GROSSUNITS",
    "fromUom": "0",
    "toUom": "10000",
    "rate": "500"
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
            # print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred for tenant ID: {tenant_id}")
        print(e)
    
    # Wait for 1 second before making the next request
    time.sleep(5)  # Adjust the wait time as needed