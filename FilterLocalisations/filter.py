import json, requests
from collections import defaultdict


def fetchMessages():
    # Endpoint URL
    url = "http://localhost:8082/localization/messages/v1/_search?locale=en_IN&tenantId=ca"

    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    body={
  "RequestInfo": {
    "apiId": "Rainmaker",
    "ver": ".01",
    "ts": "",
    "action": "_create",
    "did": "1",
    "key": "",
    "msgId": "20170310130900|en_IN",
    "authToken": "a4c35063-6a87-4671-a63b-8b92de760a4f"
  }
}

    response=requests.post(url, headers, json=body)

    messages=response.json()["messages"]

    # Write grouped results to a new JSON file
    with open("localisations.json", "w") as output_file:
        json.dump(messages, output_file, indent=4)

    print("Fresh messages written to localisations.json")

    pass


# fetchMessages()


# Sample data
with open("localisations.json", "r") as file:
    data = json.load(file)

# Function to filter objects with specific word in message
def filter_by_message(data, keyword):
    return [item for item in data if keyword.lower() in item["message"].lower()]

# Specify the keyword to search
keyword = "House/Door No."

# Get filtered results
filtered_results = filter_by_message(data, keyword)

# Group results by module
grouped_by_module = defaultdict(list)
for item in filtered_results:
    grouped_by_module[item["module"]].append(item)

# Convert defaultdict to regular dictionary for JSON compatibility
grouped_by_module = dict(grouped_by_module)

# Write grouped results to a new JSON file
with open("grouped_results.json", "w") as output_file:
    json.dump(grouped_by_module, output_file, indent=4)

print("Grouped results written to grouped_results.json")
