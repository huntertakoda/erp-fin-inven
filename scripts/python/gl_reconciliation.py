import pandas as pd

# reconcile general ledger accounts

def reconcile_accounts(csv_path):
    
    # load data
    
    general_ledger = pd.read_csv(csv_path)

    # standardize column names
    
    general_ledger.columns = general_ledger.columns.str.strip().str.lower().str.replace(" ", "_")

    # group by account_id and calculate total debits and credits
    
    grouped = general_ledger.groupby("account_id").agg({
        "debit_amount": "sum",
        "credit_amount": "sum"
    }).reset_index()

    # find mismatched accounts
    
    mismatches = grouped[grouped["debit_amount"] != grouped["credit_amount"]]

    # output results
    
    if not mismatches.empty:
        print("Reconciliation mismatches found:")
        print(mismatches)
    else:
        print("All accounts are reconciled.")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_general_ledger_data.csv"
    reconcile_accounts(input_csv)
