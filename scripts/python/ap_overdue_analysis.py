import pandas as pd
from datetime import datetime

# analyze overdue invoices in accounts payable

def analyze_overdue_invoices(csv_path, output_path):
    
    # load data
    
    accounts_payable = pd.read_csv(csv_path)

    # standardize column names
    
    accounts_payable.columns = accounts_payable.columns.str.strip().str.lower().str.replace(" ", "_")

    # convert due_date to datetime
    
    accounts_payable["due_date"] = pd.to_datetime(accounts_payable["due_date"])

    # find overdue invoices
    
    today = datetime.now()
    overdue_invoices = accounts_payable[accounts_payable["due_date"] < today]

    # save overdue invoices to a new file
    
    overdue_invoices.to_csv(output_path, index=False)
    print(f"Overdue invoices saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_accounts_payable_data.csv"
    output_csv = "C:/data/erpfin/overdue_accounts_payable_data.csv"
    analyze_overdue_invoices(input_csv, output_csv)
