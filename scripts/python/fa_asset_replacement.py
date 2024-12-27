import pandas as pd

# identify assets for replacement

def identify_replacements(csv_path, output_path):
    
    # load data
    
    fixed_assets = pd.read_csv(csv_path)

    # standardize column names
    
    fixed_assets.columns = fixed_assets.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate remaining lifespan
    
    fixed_assets["remaining_years"] = fixed_assets["lifespan_years"] - (2024 - pd.to_datetime(fixed_assets["purchase_date"]).dt.year)

    # identify assets for replacement
    
    replacements = fixed_assets[fixed_assets["remaining_years"] <= 0]

    # save replacement list
    
    replacements.to_csv(output_path, index=False)
    print(f"Assets needing replacement saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_fixed_assets_data.csv"
    output_csv = "C:/data/erpfin/assets_for_replacement.csv"
    identify_replacements(input_csv, output_csv)


