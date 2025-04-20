import pandas as pd
import itertools
import json
import os

DATA_FILE = "pt_data.csv"
PRIMARY_KEY = "propertyType"

def generate_trade_based_json(csv_file, output_prefix, primary_column):
    df = pd.read_csv(csv_file)
    df_cleaned = df.dropna(how='all')

    column_data = {
        col: df_cleaned[col].dropna().astype(str).unique().tolist()
        for col in df_cleaned.columns
    }

    column_data = {
        col: [val for val in values if val.strip() != ""]
        for col, values in column_data.items()
    }

    print("📊 Column data:")
    for col, values in column_data.items():
        print("  {}: {}".format(col, values))

    if primary_column not in column_data or not column_data[primary_column]:
        print("❌ Column '{}' missing or empty.".format(primary_column))
        return

    trade_types = column_data[primary_column]
    other_columns = {k: v for k, v in column_data.items() if k != primary_column and len(v) > 0}

    combinations = list(itertools.product(*other_columns.values()))
    print("🔁 Total combinations possible (excluding tradeType):", len(combinations))
    if not combinations:
        print("❌ No valid combinations could be created.")
        return

    os.makedirs("output_json", exist_ok=True)
    output = []

    for trade in trade_types:
        for combo in combinations:
            obj = {primary_column: trade}
            obj.update({k: combo[i] for i, k in enumerate(other_columns)})
            output.append(obj)
            print("🧩 {}".format(obj))

    output_file = "output_json/{}_output.json".format(output_prefix)
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)

    print("✅ Generated {} records.".format(len(output)))

# Example usage
generate_trade_based_json(DATA_FILE, "test_output", PRIMARY_KEY)
