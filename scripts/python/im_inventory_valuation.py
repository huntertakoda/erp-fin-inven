import pandas as pd

# calculate inventory valuation

def calculate_inventory_valuation(csv_path, output_path):
    
    # load data
    
    inventory = pd.read_csv(csv_path)

    # standardize column names
    
    inventory.columns = inventory.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate total valuation
    
    inventory["total_valuation"] = inventory["stock_level"] * inventory["price_per_unit"]

    # save inventory valuation
    
    inventory.to_csv(output_path, index=False)
    print(f"Inventory valuation saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_inventory_management_data.csv"
    output_csv = "C:/data/erpfin/inventory_valuation.csv"
    calculate_inventory_valuation(input_csv, output_csv)
