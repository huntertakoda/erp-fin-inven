import pandas as pd

# update stock levels and identify low-stock items

def update_stock_levels(csv_path, output_path, low_stock_threshold=50):
    
    # load data
    
    inventory = pd.read_csv(csv_path)

    # standardize column names
    
    inventory.columns = inventory.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate low-stock items
    
    inventory["is_low_stock"] = inventory["stock_level"] < low_stock_threshold

    # save updated inventory data
    
    inventory.to_csv(output_path, index=False)
    print(f"Stock levels updated and saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_inventory_management_data.csv"
    output_csv = "C:/data/erpfin/updated_inventory_management_data.csv"
    update_stock_levels(input_csv, output_csv)
