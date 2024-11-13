import pandas as pd
import json

# Read data from JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to an Excel file
excel_file = 'output.xlsx'  # File name for the Excel file
df.to_excel(excel_file, index=False, columns=["code", "message", "module", "locale"])

print(f"Excel file '{excel_file}' created successfully.")
