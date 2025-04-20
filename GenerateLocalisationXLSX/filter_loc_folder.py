import json
from collections import defaultdict
from pathlib import Path

# Load the JSON data
input_file = "localizations.json"
output_dir = "filtered_modules"

# Create an output directory if it doesn't exist
Path(output_dir).mkdir(exist_ok=True)

# Read the input JSON file
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Organize data by module codes
module_data = defaultdict(list)
for item in data:
    module_code = item["module"]
    module_data[module_code].append(item)

# Write filtered data into separate JSON files
for module_code, records in module_data.items():
    output_file = Path(output_dir) / f"{module_code}.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)

print(f"Filtered JSON files are saved in the '{output_dir}' directory.")
