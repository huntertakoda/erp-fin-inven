# create a trigger to update stock value in inventory management after stock level change

create or replace function update_stock_value()
returns trigger as $$
begin
    new.stock_value := new.stock_level * new.price_per_unit;
    return new;
end;
$$ language plpgsql;

create trigger stock_value_update
before insert or update on inventory_data
for each row
execute function update_stock_value();

# create a trigger to log overdue invoices in accounts payable

create or replace function log_overdue_invoices()
returns trigger as $$
begin
    if new.due_date::date < now()::date and new.payment_status = 'pending' then
        insert into overdue_invoices_log (invoice_id, vendor_id, vendor_name, overdue_amount, logged_date)
        values (new.invoice_id, new.vendor_id, new.vendor_name, new.invoice_amount, now());
    end if;
    return new;
end;
$$ language plpgsql;

create trigger overdue_invoice_log_trigger
after insert or update on accounts_payable
for each row
execute function log_overdue_invoices();

# create a trigger to track general ledger balance changes

create or replace function track_balance_changes()
returns trigger as $$
begin
    insert into general_ledger_audit (account_id, old_balance, new_balance, change_date)
    values (new.account_id, old.balance, new.balance, now());
    return new;
end;
$$ language plpgsql;

create trigger balance_change_audit
after update on general_ledger
for each row
execute function track_balance_changes();
