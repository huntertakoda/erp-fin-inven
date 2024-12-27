import pandas as pd

# calculate savings from early payment discounts

def optimize_discounts(csv_path, output_path):
    
    # load data
    
    accounts_payable = pd.read_csv(csv_path)

    # standardize column names
    
    accounts_payable.columns = accounts_payable.columns.str.strip().str.lower().str.replace(" ", "_")

    # assume a 2% discount for early payments within 10 days
    
    accounts_payable["potential_discount"] = accounts_payable["invoice_amount"] * 0.02
    accounts_payable["eligible_for_discount"] = accounts_payable["due_date"].apply(lambda x: pd.Timestamp.now() + pd.Timedelta(days=10) >= pd.to_datetime(x))

    # save discount optimization data
    
    accounts_payable.to_csv(output_path, index=False)
    print(f"Discount optimization data saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_accounts_payable_data.csv"
    output_csv = "C:/data/erpfin/discount_optimization.csv"
    optimize_discounts(input_csv, output_csv)
