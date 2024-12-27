# clean data by removing duplicate records in general ledger

delete from general_ledger
where ctid not in (
    select min(ctid)
    from general_ledger
    group by account_id, transaction_date, debit_amount, credit_amount
)
;

# clean data by removing rows with null values in critical columns for accounts payable

delete from accounts_payable
where vendor_id is null
   or invoice_id is null
   or invoice_amount is null
;

# transform dates in fixed assets to a consistent format (if stored as strings)

update fixed_assets
set purchase_date = to_date(purchase_date, 'YYYY-MM-DD')
where purchase_date is not null
;

# add a new column for stock value in inventory management

alter table inventory_data
add column if not exists stock_value numeric(12, 2)
;

# update stock value column based on current stock levels and prices

update inventory_data
set stock_value = stock_level * price_per_unit
;
