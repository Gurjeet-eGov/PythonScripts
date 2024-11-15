import requests
import random
import datetime
import json

def read_json(file_path):
    with open(file_path) as file: 
        payload = json.load(file)
    return payload
    

def log_response(response):
    """Log response for debugging."""
    print(f"URL: {response.url}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def prepare_update_payload(RequestInfo, sample_payload_path, 
                           obj_keyword, prev_response, mod_data_path):
    """
    Dynamically prepares the update payload by modifying the create response.

    Args:
        prev_response (dict): The original response from the create API.
        modifications (dict): A dictionary containing the modifications to apply.

    Returns:
        dict: The updated payload for the update API.
    """
    import copy

    update_payload=read_json(sample_payload_path)

    update_payload["RequestInfo"] = RequestInfo

    # Make a deep copy of the create response to avoid modifying the original
    update_payload[obj_keyword] = copy.deepcopy(prev_response)
    
    def apply_modifications(target, updates):
        """Recursively applies modifications to the target dictionary."""
        for key, value in updates.items():
            if isinstance(value, dict) and isinstance(target.get(key), dict):
                apply_modifications(target[key], value)  # Recurse for nested dicts
            else:
                target[key] = value  # Apply modification (either edit or add new key)
    
    mod_data = read_json(mod_data_path)
    # Apply the modifications
    apply_modifications(update_payload[obj_keyword][0], mod_data)

    return update_payload