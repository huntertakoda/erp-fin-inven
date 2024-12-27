import pandas as pd

# generate audit trail for general ledger

def generate_audit_trail(csv_path, output_path):
    
    # load data
    
    general_ledger = pd.read_csv(csv_path)

    # standardize column names
    
    general_ledger.columns = general_ledger.columns.str.strip().str.lower().str.replace(" ", "_")

    # create audit trail (duplicate rows with 'created' or 'updated' status)
    
    general_ledger["audit_action"] = "created"
    audit_trail = general_ledger.copy()

    # save audit trail
    
    audit_trail.to_csv(output_path, index=False)
    print(f"Audit trail saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_general_ledger_data.csv"
    output_csv = "C:/data/erpfin/general_ledger_audit_trail.csv"
    generate_audit_trail(input_csv, output_csv)
