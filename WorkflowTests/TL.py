from logic import Core
import utils

TL_obj = Core("TL")

# Main workflow
def NewTL():
    csr_login_RequestInfo = TL_obj.login_new("CSR")

    csr_create_response = TL_obj.call_api(csr_login_RequestInfo, "TL/csr_create_payload.json", TL_obj.get_endpoint("create"))["Licenses"]

    csr_update_data = utils.prepare_update_payload(RequestInfo=csr_login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_create_response, 
                        mod_data_path="TL/csr_update_data.json")

    # CSR Update
    csr_update_response = TL_obj.call_api(csr_login_RequestInfo, csr_update_data, TL_obj.get_endpoint("update"))["Licenses"]


    login_RequestInfo = TL_obj.login_new("FieldEmp")
    dv_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=csr_update_response, 
                        mod_data_path="TL/dv_update_data.json")
    


    # DV Update
    dv_update_response = TL_obj.call_api(login_RequestInfo, dv_update_data, TL_obj.get_endpoint("update"))["Licenses"]

    fi_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=dv_update_response, 
                        mod_data_path="TL/fi_update_data.json")
    
    # FI Update
    fi_update_response = TL_obj.call_api(login_RequestInfo, fi_update_data, TL_obj.get_endpoint("update"))["Licenses"]

    login_RequestInfo = TL_obj.login_new("OfficeEmp")
    ap_update_data = utils.prepare_update_payload(RequestInfo=login_RequestInfo, 
                        sample_payload_path="TL/update_payload.json", 
                        obj_keyword="Licenses",
                        prev_response=fi_update_response, 
                        mod_data_path="TL/ap_update_data.json")
    
    

    # AP Update
    ap_update_response = TL_obj.call_api(login_RequestInfo, ap_update_data, TL_obj.get_endpoint("update"))["Licenses"]

    fetch_bill_response = TL_obj.fetch_bill(csr_login_RequestInfo, ap_update_response[0]["applicationNumber"], "TL")
    collection_response = TL_obj.collect_fee(login_RequestInfo, fetch_bill_response)

NewTL()