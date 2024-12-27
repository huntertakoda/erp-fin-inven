import pandas as pd

# predict reorder needs for inventory items

def predict_reorders(csv_path, output_path):
    
    # load data
    
    inventory = pd.read_csv(csv_path)

    # standardize column names
    
    inventory.columns = inventory.columns.str.strip().str.lower().str.replace(" ", "_")

    # identify items that need reordering
    
    inventory["needs_reorder"] = inventory["stock_level"] < inventory["reorder_level"]

    # save reorder predictions
    
    inventory.to_csv(output_path, index=False)
    print(f"Reorder predictions saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_inventory_management_data.csv"
    output_csv = "C:/data/erpfin/reorder_predictions_inventory.csv"
    predict_reorders(input_csv, output_csv)
