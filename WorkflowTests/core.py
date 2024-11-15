import requests
import random
import datetime
import json

import utils

# Configuration
BASE_URL = "https://ips-demo.digit.org"
HEADERS = {"Content-Type": "application/json"}
ENDPOINTS = "endpoints.json"
STATE = "ca"
CITY = "ca.alameda"

def get_endpoint(api_name):
    with open(ENDPOINTS) as file: 
        endpoint = json.load(file)
    return endpoint[api_name]

def call_api(RequestInfo, payload, api_name):
    if isinstance(payload, str):
        payload = utils.read_json(payload)
    else:
        payload=payload
    payload["RequestInfo"] = RequestInfo
    response = requests.post(url=BASE_URL+get_endpoint(api_name), 
                             headers=HEADERS, 
                             json=payload)
    utils.log_response(response)
    return response.json()

def fetch_bill(RequestInfo, App_ID, businessService):
    payload = { "RequestInfo": RequestInfo}
    params = {
        "tenantId": CITY,
        "consumerCode": App_ID,
        "businessService": businessService
    }
    response = requests.post(url=BASE_URL+"/billing-service/bill/v2/_fetchbill", 
                             headers=HEADERS, 
                             params=params,
                             json=payload)
    utils.log_response(response)
    return response.json()

def login(username, password, tenantId, userType):
    payload = {
                "username": username,
                "password": password,
                "userType": userType,
                "tenantId": tenantId,
                "scope": "read",
                "grant_type": "password"
            }
    header = utils.read_json("login_headers.json")
    response = requests.post(url=BASE_URL+get_endpoint("login"), 
                             headers=header, 
                             data=payload)
    utils.log_response(response)
    RequestInfo = utils.read_json("RequestInfo.json")
    RequestInfo["authToken"] = response.json()["access_token"]
    RequestInfo["userInfo"] = response.json()["UserRequest"]
    return RequestInfo

def collect_fee(RequestInfo, fetchBillResponse):
    from CollectionService import payload_builder

    bill_data = fetchBillResponse["Bill"][0]
    payload = payload_builder.create(bill_data, RequestInfo)
    params = {
        "tenantId": CITY
    }
    response = requests.post(url=BASE_URL+"/collection-services/payments/_create", 
                             headers=HEADERS, 
                             params=params,
                             json=payload)
    
    utils.log_response(response)

# Main workflow
def NewTL():
    csr_login_RequestInfo = login("CSR", "Demo@123", CITY, "EMPLOYEE")

    csr_create_response = call_api(csr_login_RequestInfo, "TL/csr_create_payload.json", "createTL")["Licenses"]

    csr_update_data = utils.prepare_update_payload(RequestInfo=csr_login_RequestInfo, 
                           sample_payload_path="TL/update_payload.json", 
                           obj_keyword="Licenses",
                           prev_response=csr_create_response, 
                           mod_data_path="TL/csr_update_data.json")

    # CSR Update
    csr_update_response = call_api(csr_login_RequestInfo, csr_update_data, "updateTL")["Licenses"]


    login_RequestInfo = login("FieldEmployee", "Demo@123", CITY, "EMPLOYEE")
    dv_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_update_response, 
                        mod_data_path="TL/dv_update_data.json")
    


    # DV Update
    dv_update_response = call_api(login_RequestInfo, dv_update_data, "updateTL")["Licenses"]

    fi_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=dv_update_response, 
                        mod_data_path="TL/fi_update_data.json")
    
    # FI Update
    fi_update_response = call_api(login_RequestInfo, fi_update_data, "updateTL")["Licenses"]

    login_RequestInfo = login("OfficeEmployee", "Demo@123", CITY, "EMPLOYEE")
    ap_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=fi_update_response, 
                        mod_data_path="TL/ap_update_data.json")
    
    

    # AP Update
    ap_update_response = call_api(login_RequestInfo, ap_update_data, "updateTL")["Licenses"]

    fetch_bill_response = fetch_bill(csr_login_RequestInfo, ap_update_response[0]["applicationNumber"], "TL")
    collection_response = collect_fee(login_RequestInfo, fetch_bill_response)


NewTL()