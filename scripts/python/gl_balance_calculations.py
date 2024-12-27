import pandas as pd

# calculate balances for general ledger

def calculate_balances(csv_path, output_path):
    
    # load data
    
    general_ledger = pd.read_csv(csv_path)

    # standardize column names to ensure compatibility
    
    general_ledger.columns = general_ledger.columns.str.strip().str.lower().str.replace(" ", "_")

    # calculate balances
    
    general_ledger["balance"] = general_ledger["debit_amount"] - general_ledger["credit_amount"]

    # save updated data
    
    general_ledger.to_csv(output_path, index=False)
    print(f"Balances calculated and saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_general_ledger_data.csv"
    output_csv = "C:/data/erpfin/updated_general_ledger_data.csv"
    calculate_balances(input_csv, output_csv)
