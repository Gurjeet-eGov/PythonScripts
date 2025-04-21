import json
import logging
import random
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    filename='response_log.txt',  # Log file name
    filemode='w',
    level=logging.INFO,           # Set logging level to INFO (or DEBUG for more detailed logs)
    format='%(asctime)s - %(message)s',  # Log format with timestamp
)

def read_json(file_path):
    with open(file_path) as file: 
        payload = json.load(file)
    return payload
    
def randomize_epoch(from_epoch, to_epoch, count):
    
    """
    Generate a list of random epoch timestamps, shuffling days and months.

    :param from_epoch: Start epoch time (inclusive).
    :param to_epoch: End epoch time (exclusive).
    :param count: Number of random epochs to generate.
    :return: List of random epoch timestamps.
    """
    
    # Convert to seconds for datetime
    from_epoch = from_epoch / 1000
    to_epoch = to_epoch / 1000

    # Convert to datetime
    start_date = datetime.fromtimestamp(from_epoch)
    end_date = datetime.fromtimestamp(to_epoch)

    # Generate a list of dates
    all_days = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    # Convert back to milliseconds
    random_days = random.sample(all_days, k=count)
    random_epochs_ms = [int(day.timestamp() * 1000) for day in random_days]
    
    # Convert selected dates to epoch timestamps (defaulting to midnight)
    return random_epochs_ms

def log_response(response):
    
    """Log response details to a file."""
    try:
        # Extract response details
        url = response.url
        status_code = response.status_code
        request_body = response.request.body
        response_content = response.json()

        # Log the details
        logging.info(f"URL: {url}")
        logging.info(f"Status Code: {status_code}")
        logging.info(f"Request Body: {request_body}")
        logging.info(f"Response: {response_content}\n")

    except Exception as e:
        # Log any exceptions while logging the response
        logging.error(f"Failed to log response: {e}")

def generate_RequestInfo(authToken, userReqInfo):
    from dataclasses import dataclass, field, asdict
    from typing import Dict

    @dataclass
    class ReqInfo:
        authToken: str
        apiId: str = ""
        ver: str = ".01"
        ts: str = ""
        action: str = "_create"
        did: str = "1"
        key: str = ""
        msgId: str = "20170310130900|en_IN"
        userInfo: Dict = field(default_factory=dict)

    return asdict(
            ReqInfo(
            authToken=authToken,
            userInfo=userReqInfo
        )
    )

def mod_json(payload, key, new_value):
    """
    Recursively searches for the key in a nested payload and updates its value.

    :param payload: The nested dictionary/list where the key may be found.
    :param key: The key to search for.
    :param new_value: The new value to assign to the key.
    :return: The updated payload.
    """
    if isinstance(payload, dict):  # If the payload is a dictionary
        for k, v in payload.items():
            if k == key:
                payload[k] = new_value  # Update value if key matches
            else:
                mod_json(v, key, new_value)  # Recursively search in nested structures

    elif isinstance(payload, list):  # If the payload is a list
        for item in payload:
            mod_json(item, key, new_value)  # Recursively search in list items

    return payload

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

    def apply_mods(target, updates):
        """Recursively applies modifications to the target dictionary."""
        for key, value in updates.items():
            if isinstance(value, dict) and isinstance(target.get(key), dict):
                apply_mods(target[key], value)  # Recurse for nested dicts
            else:
                target[key] = value  # Apply modification (either edit or add new key)
    
    # Make a deep copy of the create response to avoid modifying the original
    update_payload[obj_keyword] = copy.deepcopy(prev_response)
    
    mod_data = read_json(mod_data_path)
    # Apply the modifications
    apply_mods(update_payload[obj_keyword][0], mod_data)

    return update_payload