# extract data from general ledger for etl pipeline

select *
from general_ledger
;

# transform general ledger data by calculating net amounts

select 
    account_id,
    account_name,
    account_type,
    transaction_date,
    debit_amount,
    credit_amount,
    (debit_amount - credit_amount) as net_amount
from general_ledger
;

# load transformed data into a staging table

create table if not exists staging_general_ledger as
select 
    account_id,
    account_name,
    account_type,
    transaction_date,
    debit_amount,
    credit_amount,
    (debit_amount - credit_amount) as net_amount
from general_ledger
;

# update inventory data by recalculating stock value

update inventory_data
set stock_value = stock_level * price_per_unit
;

# insert data into accounts payable analytics table

insert into accounts_payable_analytics (vendor_id, vendor_name, overdue_amount)
select 
    vendor_id,
    vendor_name,
    sum(invoice_amount) as overdue_amount
from accounts_payable
where due_date::date < now()::date
group by vendor_id, vendor_name
;
