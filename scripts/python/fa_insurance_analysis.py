import pandas as pd

# analyze insurance coverage for fixed assets

def analyze_insurance(csv_path, output_path):
    
    # load data
    
    fixed_assets = pd.read_csv(csv_path)

    # standardize column names
    
    fixed_assets.columns = fixed_assets.columns.str.strip().str.lower().str.replace(" ", "_")

    # recommend insurance coverage (assume 1.2x asset cost for replacement coverage)
    
    fixed_assets["recommended_coverage"] = fixed_assets["acquisition_cost"] * 1.2

    # save insurance analysis
    
    fixed_assets.to_csv(output_path, index=False)
    print(f"Insurance analysis saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_fixed_assets_data.csv"
    output_csv = "C:/data/erpfin/insurance_analysis_fixed_assets.csv"
    analyze_insurance(input_csv, output_csv)
