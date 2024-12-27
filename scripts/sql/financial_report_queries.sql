# generate trial balance report from general ledger

select 
    account_type,
    account_name,
    sum(debit_amount) as total_debits,
    sum(credit_amount) as total_credits,
    (sum(debit_amount) - sum(credit_amount)) as net_balance
from general_ledger
group by account_type, account_name
order by account_type, account_name
;

# generate accounts payable aging report

select 
    vendor_name,
    sum(case when due_date::date < now()::date then invoice_amount else 0 end) as overdue_amount,
    sum(case when due_date::date >= now()::date then invoice_amount else 0 end) as current_amount,
    count(*) as total_invoices
from accounts_payable
group by vendor_name
order by overdue_amount desc
;

# generate fixed assets depreciation summary

select 
    asset_type,
    count(*) as total_assets,
    sum(acquisition_cost) as total_acquisition_cost,
    sum(acquisition_cost * (depreciation_rate / 100)) as total_depreciation
from fixed_assets
group by asset_type
order by total_acquisition_cost desc
;

# generate inventory value report by category

select 
    category,
    sum(stock_level * price_per_unit) as total_stock_value,
    count(*) as total_products
from inventory_data
group by category
order by total_stock_value desc
;
