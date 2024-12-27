import pandas as pd

# track the lifecycle of fixed assets

def track_lifecycle(csv_path, output_path):
    
    # load data

    fixed_assets = pd.read_csv(csv_path)

    # standardize column names
    
    fixed_assets.columns = fixed_assets.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate remaining years
    
    fixed_assets["remaining_years"] = fixed_assets["lifespan_years"] - (2024 - pd.to_datetime(fixed_assets["purchase_date"]).dt.year)

    # identify assets nearing end of lifecycle
    
    nearing_end = fixed_assets[fixed_assets["remaining_years"] <= 1]

    # save lifecycle tracking data
    
    nearing_end.to_csv(output_path, index=False)
    print(f"Lifecycle tracking saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_fixed_assets_data.csv"
    output_csv = "C:/data/erpfin/fixed_assets_lifecycle_tracking.csv"
    track_lifecycle(input_csv, output_csv)
