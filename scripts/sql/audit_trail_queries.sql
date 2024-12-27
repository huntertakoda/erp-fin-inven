# create an audit trail table for general ledger changes

create table if not exists general_ledger_audit (
    audit_id serial primary key,
    account_id uuid not null,
    old_balance numeric(12, 2),
    new_balance numeric(12, 2),
    change_date timestamp default now(),
    changed_by varchar(50)
)
;

# log changes to balances in general ledger

insert into general_ledger_audit (account_id, old_balance, new_balance, change_date, changed_by)
select 
    old.account_id,
    old.balance as old_balance,
    new.balance as new_balance,
    now() as change_date,
    'system_user' as changed_by
from general_ledger old
join general_ledger new
on old.account_id = new.account_id
where old.balance <> new.balance
;

# create an audit trail table for overdue invoices

create table if not exists overdue_invoices_log (
    log_id serial primary key,
    invoice_id uuid not null,
    vendor_id uuid not null,
    vendor_name varchar(255),
    overdue_amount numeric(12, 2),
    logged_date timestamp default now()
)
;

# log all overdue invoices from accounts payable

insert into overdue_invoices_log (invoice_id, vendor_id, vendor_name, overdue_amount, logged_date)
select 
    invoice_id,
    vendor_id,
    vendor_name,
    invoice_amount as overdue_amount,
    now() as logged_date
from accounts_payable
where due_date::date < now()::date and payment_status = 'pending'
;
