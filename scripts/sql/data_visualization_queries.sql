# prepare data for financial summary visualization

select 
    sum(debit_amount) as total_debit,
    sum(credit_amount) as total_credit,
    (sum(debit_amount) - sum(credit_amount)) as net_balance
from general_ledger
;

# prepare overdue invoices data for visualization

select 
    vendor_name,
    count(*) as total_overdue_invoices,
    sum(invoice_amount) as total_overdue_amount
from accounts_payable
where due_date::date < now()::date
group by vendor_name
order by total_overdue_amount desc
;

# prepare fixed assets depreciation data for visualization

select 
    asset_type,
    sum(acquisition_cost) as total_acquisition_cost,
    sum(acquisition_cost * (depreciation_rate / 100)) as total_depreciation
from fixed_assets
group by asset_type
order by total_acquisition_cost desc
;

# prepare inventory value by category for visualization

select 
    category,
    sum(stock_level * price_per_unit) as total_stock_value,
    avg(price_per_unit) as average_price_per_unit
from inventory_data
group by category
order by total_stock_value desc
;
