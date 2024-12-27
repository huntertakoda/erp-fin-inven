import pandas as pd

# optimize warehouse utilization

def optimize_warehouse(csv_path, output_path, max_capacity=5000):
    
    # load data
    
    inventory = pd.read_csv(csv_path)

    # standardize column names
    
    inventory.columns = inventory.columns.str.strip().str.lower().str.replace(" ", "_")

    # check if unit_volume exists
    
    if "unit_volume" not in inventory.columns:
        print("Column 'unit_volume' not found. Using default volume of 1 per unit.")
        inventory["unit_volume"] = 1  # assign default value if column is missing

    # calculate total inventory usage
    
    inventory["space_usage"] = inventory["stock_level"] * inventory["unit_volume"]
    total_space_usage = inventory["space_usage"].sum()

    # identify overstocked and understocked items
    
    inventory["overstocked"] = inventory["space_usage"] > max_capacity
    inventory["understocked"] = inventory["stock_level"] < inventory["reorder_level"]

    # save warehouse optimization data
    
    inventory.to_csv(output_path, index=False)
    print(f"Warehouse optimization data saved to {output_path}")
    print(f"Total warehouse space used: {total_space_usage}/{max_capacity}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_inventory_management_data.csv"
    output_csv = "C:/data/erpfin/warehouse_optimization.csv"
    optimize_warehouse(input_csv, output_csv)
