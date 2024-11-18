from logic import Core
import utils

TL_obj = Core("TL")

# Main workflow
def NewTL():
    
    csr_login_RequestInfo = TL_obj.login("CSR")

    # CSR Create
    csr_create_response = TL_obj.call_api(csr_login_RequestInfo, "TL/csr_create_payload.json", TL_obj.get_endpoint("create"))["Licenses"]
    
    # CSR Update
    csr_update_data = utils.prepare_update_payload(RequestInfo=csr_login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_create_response, 
                        mod_data_path="TL/csr_update_data.json")
    csr_update_response = TL_obj.call_api(csr_login_RequestInfo, csr_update_data, TL_obj.get_endpoint("update"))["Licenses"]


    login_RequestInfo = TL_obj.login("FieldEmp")

    # DV Update
    dv_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_update_response, 
                        mod_data_path="TL/dv_update_data.json")
    dv_update_response = TL_obj.call_api(login_RequestInfo, dv_update_data, TL_obj.get_endpoint("update"))["Licenses"]

    # FI Update
    fi_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=dv_update_response, 
                        mod_data_path="TL/fi_update_data.json")
    fi_update_response = TL_obj.call_api(login_RequestInfo, fi_update_data, TL_obj.get_endpoint("update"))["Licenses"]
    # logout FieldEmp
    TL_obj.logout(login_RequestInfo)
    

    login_RequestInfo = TL_obj.login("OfficeEmp")
    # AP Update payload
    ap_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=fi_update_response, 
                        mod_data_path="TL/ap_update_data.json")
    ap_update_response = TL_obj.call_api(login_RequestInfo, ap_update_data, 
                                         TL_obj.get_endpoint("update"))["Licenses"]
    # logout OfficeEmp
    TL_obj.logout(login_RequestInfo)

    fetch_bill_response = TL_obj.fetch_bill(csr_login_RequestInfo, ap_update_response[0]["applicationNumber"], "TL")
    collection_response = TL_obj.collect_fee(login_RequestInfo, fetch_bill_response)
    # logout CSR
    TL_obj.logout(csr_login_RequestInfo)

def NewTL_mod(epoch_key, epoch_value):
    
    csr_login_RequestInfo = TL_obj.login("CSR")

    # CSR Create
    csr_create_response = TL_obj.call_api(csr_login_RequestInfo, "TL/csr_create_payload.json", TL_obj.get_endpoint("create"))["Licenses"]

    # CSR Update
    csr_update_data = utils.prepare_update_payload(RequestInfo=csr_login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_create_response, 
                        mod_data_path="TL/csr_update_data.json")

    
    csr_update_response = TL_obj.call_api(csr_login_RequestInfo, csr_update_data, TL_obj.get_endpoint("update"))["Licenses"]


    login_RequestInfo = TL_obj.login("FieldEmp")
    # DV Update
    dv_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_update_response, 
                        mod_data_path="TL/dv_update_data.json")

    dv_update_response = TL_obj.call_api(login_RequestInfo, dv_update_data, TL_obj.get_endpoint("update"))["Licenses"]
    
    
    # FI Update
    fi_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=dv_update_response, 
                        mod_data_path="TL/fi_update_data.json")
    
    fi_update_response = TL_obj.call_api(login_RequestInfo, fi_update_data, TL_obj.get_endpoint("update"))["Licenses"]
    # logout FieldEmp
    TL_obj.logout(login_RequestInfo)

    
    login_RequestInfo = TL_obj.login("OfficeEmp")
    # AP Update payload
    ap_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=fi_update_response, 
                        mod_data_path="TL/ap_update_data.json")
    
    ap_update_data = utils.mod_json(ap_update_data, epoch_key, epoch_value)

    ap_update_response = TL_obj.call_api(login_RequestInfo, ap_update_data, 
                                         TL_obj.get_endpoint("update"))["Licenses"]

    # logout OfficeEmp
    TL_obj.logout(login_RequestInfo)


    fetch_bill_response = TL_obj.fetch_bill(csr_login_RequestInfo, ap_update_response[0]["applicationNumber"], "TL")
    collection_response = TL_obj.collect_fee(csr_login_RequestInfo, fetch_bill_response)

    # logout CSR
    TL_obj.logout(csr_login_RequestInfo)
