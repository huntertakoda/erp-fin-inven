import pandas as pd

# match invoices and identify discrepancies

def match_invoices(csv_path, output_path):
    
    # load data
    
    accounts_payable = pd.read_csv(csv_path)

    # standardize column names
    
    accounts_payable.columns = accounts_payable.columns.str.strip().str.lower().str.replace(" ", "_")

    # find discrepancies where payment status doesn't match expected conditions
    
    discrepancies = accounts_payable[
        (accounts_payable["payment_status"].str.lower() == "paid") &
        (accounts_payable["invoice_amount"] > 0)
    ]

    # save discrepancies to a new file
    
    discrepancies.to_csv(output_path, index=False)
    print(f"Discrepancies saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_accounts_payable_data.csv"
    output_csv = "C:/data/erpfin/discrepancies_accounts_payable_data.csv"
    match_invoices(input_csv, output_csv)
