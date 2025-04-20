import json
import subprocess
from pathlib import Path
import tempfile

# Configuration
filtered_modules_dir = "filtered_modules"
base_curl_command = [
    "curl",
    "--location",
    "localhost:8082/assam/localization/messages/v1/_upsert",
    "--header",
    "Content-Type: application/json",
]

# Iterate over each JSON file in the filtered_modules directory
for json_file in Path(filtered_modules_dir).glob("*.json"):
    # Read the JSON file
    with open(json_file, "r", encoding="utf-8") as file:
        messages = json.load(file)
    
    # Prepare the data for the cURL request
    payload = {
        "RequestInfo": {
            "apiId": "",
            "ver": ".01",
            "ts": "",
            "action": "_create",
            "did": "1",
            "key": "",
            "msgId": "20170310130900|en_IN",
            "authToken": "6e7031e4-e0f0-4ead-a0fe-c169c0698b44",
            "userInfo": {
                "id": 95,
                "uuid": "9dea0b44-217d-45a3-b9bc-ac28703bc7ef",
                "userName": "SUPERUSER",
                "name": "SUPERUSER",
                "mobileNumber": "9035169728",
                "emailId": None,
                "locale": None,
                "type": "EMPLOYEE",
                "roles": [
                    {"name": "SUPER USER", "code": "SUPERUSER", "tenantId": "as"}
                ],
                "active": True,
                "tenantId": "as",
                "permanentCity": None,
            },
        },
        "tenantId": "as",
        "messages": messages,
    }

    # Write the payload to a temporary file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as temp_file:
        json.dump(payload, temp_file, ensure_ascii=False, indent=4)
        temp_file_path = temp_file.name

    # Add the file to the cURL command
    curl_command = base_curl_command + ["--data", f"@{temp_file_path}"]

    # Execute the cURL command
    result = subprocess.run(curl_command, capture_output=True, text=True)

    # Print the result of the cURL command
    print(f"File: {json_file.name}")
    print(f"Response: {result.stdout}")
    if result.stderr:
        print(f"Error: {result.stderr}")
    print("-" * 80)

    # Clean up the temporary file
    Path(temp_file_path).unlink()
