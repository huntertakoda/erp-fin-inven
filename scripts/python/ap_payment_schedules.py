import pandas as pd

# generate payment schedules for accounts payable

def generate_payment_schedules(csv_path, output_path):
    
    # load data
    
    accounts_payable = pd.read_csv(csv_path)

    # standardize column names
    
    accounts_payable.columns = accounts_payable.columns.str.strip().str.lower().str.replace(" ", "_")

    # create a new column for payment status
    
    accounts_payable["payment_schedule"] = accounts_payable["due_date"]

    # save updated data
    
    accounts_payable.to_csv(output_path, index=False)
    print(f"Payment schedules saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_accounts_payable_data.csv"
    output_csv = "C:/data/erpfin/updated_accounts_payable_data.csv"
    generate_payment_schedules(input_csv, output_csv)
