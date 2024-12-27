import pandas as pd

# identify and log errors in general ledger

def handle_gl_errors(csv_path, error_log_path):
    
    # load data
    
    general_ledger = pd.read_csv(csv_path)

    # standardize column names
    
    general_ledger.columns = general_ledger.columns.str.strip().str.lower().str.replace(" ", "_")

    # identify errors (e.g., missing values in critical columns)
    
    errors = general_ledger[
        general_ledger["account_id"].isnull() |
        general_ledger["transaction_date"].isnull() |
        ((general_ledger["debit_amount"].fillna(0) == 0) & (general_ledger["credit_amount"].fillna(0) == 0))
    ]

    # save errors to a log file
    
    errors.to_csv(error_log_path, index=False)
    print(f"Errors logged to {error_log_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_general_ledger_data.csv"
    error_log_csv = "C:/data/erpfin/general_ledger_error_log.csv"
    handle_gl_errors(input_csv, error_log_csv)
