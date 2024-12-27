import pandas as pd
from datetime import datetime

# forecast future cash outflows for accounts payable

def forecast_cash_outflows(csv_path, output_path):
    
    # load data
    
    accounts_payable = pd.read_csv(csv_path)

    # standardize column names
    
    accounts_payable.columns = accounts_payable.columns.str.strip().str.lower().str.replace(" ", "_")

    # convert due_date to datetime
    
    accounts_payable["due_date"] = pd.to_datetime(accounts_payable["due_date"])

    # group by due month and calculate total cash outflows
    
    accounts_payable["due_month"] = accounts_payable["due_date"].dt.to_period("M")
    cash_flow_forecast = accounts_payable.groupby("due_month").agg(
        total_outflow=("invoice_amount", "sum")
    ).reset_index()

    # save cash flow forecast
    
    cash_flow_forecast.to_csv(output_path, index=False)
    print(f"Cash flow forecast saved to {output_path}")

if __name__ == "__main__":
    input_csv = "C:/data/erpfin/cleaned_accounts_payable_data.csv"
    output_csv = "C:/data/erpfin/cash_flow_forecast.csv"
    forecast_cash_outflows(input_csv, output_csv)
