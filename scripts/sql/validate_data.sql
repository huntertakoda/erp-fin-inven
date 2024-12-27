# validate data integrity in general ledger

select *
from general_ledger
where account_id is null
   or account_name is null
   or account_type is null
   or transaction_date is null
   or debit_amount is null
   or credit_amount is null
   or balance is null
;

# validate data integrity in accounts payable

select *
from accounts_payable
where vendor_id is null
   or vendor_name is null
   or invoice_id is null
   or invoice_amount is null
   or due_date is null
   or payment_status is null
;

# validate data integrity in fixed assets

select *
from fixed_assets
where asset_id is null
   or asset_name is null
   or asset_type is null
   or acquisition_cost is null
   or lifespan_years is null
   or depreciation_rate is null
   or purchase_date is null
;

# validate data integrity in inventory management

select *
from inventory_data
where product_id is null
   or product_name is null
   or category is null
   or stock_level is null
   or reorder_level is null
   or price_per_unit is null
   or last_updated is null
;
