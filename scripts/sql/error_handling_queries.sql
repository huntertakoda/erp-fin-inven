# handle missing or invalid data in general ledger by replacing null values

update general_ledger
set debit_amount = 0
where debit_amount is null
;

update general_ledger
set credit_amount = 0
where credit_amount is null
;

# log errors for invalid due dates in accounts payable

create table if not exists error_logs (
    error_id serial primary key,
    table_name varchar(50),
    error_description text,
    record_id uuid,
    logged_date timestamp default now()
)
;

insert into error_logs (table_name, error_description, record_id, logged_date)
select 
    'accounts_payable' as table_name,
    'invalid due date' as error_description,
    vendor_id as record_id,
    now() as logged_date
from accounts_payable
where due_date::date is null or due_date::date > now() + interval '10 years'
;

# handle negative stock levels in inventory management

update inventory_data
set stock_level = 0
where stock_level < 0
;

# log errors for assets with negative acquisition cost

insert into error_logs (table_name, error_description, record_id, logged_date)
select 
    'fixed_assets' as table_name,
    'negative acquisition cost' as error_description,
    asset_id as record_id,
    now() as logged_date
from fixed_assets
where acquisition_cost < 0
;
