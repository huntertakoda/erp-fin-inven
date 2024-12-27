# calculate total debit and credit amounts in general ledger

select 
    sum(debit_amount) as total_debit,
    sum(credit_amount) as total_credit
from general_ledger
;

# calculate total outstanding invoice amount in accounts payable

select 
    sum(invoice_amount) as total_outstanding_invoices
from accounts_payable
where payment_status = 'pending'
;

# calculate total acquisition cost and total depreciation in fixed assets

select 
    sum(acquisition_cost) as total_acquisition_cost,
    sum(acquisition_cost * (depreciation_rate / 100)) as total_depreciation
from fixed_assets
;

# calculate total stock value in inventory management

select 
    sum(stock_level * price_per_unit) as total_stock_value
from inventory_data
;
