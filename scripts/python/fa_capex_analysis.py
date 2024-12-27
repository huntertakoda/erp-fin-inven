import pandas as pd

# analyze capital expenditure for fixed assets

def analyze_capex(csv_path, output_path):
    
    # load data
    
    fixed_assets = pd.read_csv(csv_path)

    # standardize column names
    
    fixed_assets.columns = fixed_assets.columns.str.strip().str.lower().str.replace(" ", "_")

    # aggregate acquisition cost by asset type
    
    capex_analysis = fixed_assets.groupby("asset_type").agg(
        total_acquisition_cost=("acquisition_cost", "sum"),
        average_acquisition_cost=("acquisition_cost", "mean"),
        count_of_assets=("asset_id", "count")
    ).reset_index()

    # save capex analysis
    
    capex_analysis.to_csv(output_path, index=False)
    print(f"CAPEX analysis saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_fixed_assets_data.csv"
    output_csv = "C:/data/erpfin/capex_analysis_fixed_assets.csv"
    analyze_capex(input_csv, output_csv)
