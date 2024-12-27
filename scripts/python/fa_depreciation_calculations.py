import pandas as pd

# calculate depreciation for fixed assets

def calculate_depreciation(csv_path, output_path):
    
    # load data
    
    fixed_assets = pd.read_csv(csv_path)

    # standardize column names
    
    fixed_assets.columns = fixed_assets.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate annual depreciation
    
    fixed_assets["annual_depreciation"] = fixed_assets["acquisition_cost"] / fixed_assets["lifespan_years"]

    # calculate accumulated depreciation
    
    fixed_assets["accumulated_depreciation"] = fixed_assets["annual_depreciation"] * (2024 - pd.to_datetime(fixed_assets["purchase_date"]).dt.year)

    # save updated data
    
    fixed_assets.to_csv(output_path, index=False)
    print(f"Depreciation calculations saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_fixed_assets_data.csv"
    output_csv = "C:/data/erpfin/updated_fixed_assets_data.csv"
    calculate_depreciation(input_csv, output_csv)
