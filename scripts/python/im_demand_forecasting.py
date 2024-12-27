import pandas as pd

# forecast demand for inventory items

def forecast_demand(csv_path, output_path, window=3):
    
    # load data
    
    inventory = pd.read_csv(csv_path)

    # standardize column names
    
    inventory.columns = inventory.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate moving average demand
    
    inventory["forecasted_demand"] = inventory["stock_level"].rolling(window=window).mean()

    # save demand forecast
    
    inventory.to_csv(output_path, index=False)
    print(f"Demand forecasts saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_inventory_management_data.csv"
    output_csv = "C:/data/erpfin/demand_forecasting_inventory.csv"
    forecast_demand(input_csv, output_csv)
