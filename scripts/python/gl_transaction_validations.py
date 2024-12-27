import pandas as pd

# validate transactions in general ledger

def validate_transactions(csv_path):
    
    # load data
    
    general_ledger = pd.read_csv(csv_path)

    # standardize column names
    
    general_ledger.columns = general_ledger.columns.str.strip().str.lower().str.replace(" ", "_")

    # find invalid transactions (where both debit and credit are null or zero)
    
    invalid_transactions = general_ledger[
        (general_ledger["debit_amount"].fillna(0) == 0) &
        (general_ledger["credit_amount"].fillna(0) == 0)
    ]

    # output results
    
    if not invalid_transactions.empty:
        print("Invalid transactions found:")
        print(invalid_transactions)
    else:
        print("No invalid transactions found.")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_general_ledger_data.csv"
    validate_transactions(input_csv)
