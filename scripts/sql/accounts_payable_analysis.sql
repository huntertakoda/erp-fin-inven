# identify overdue invoices

select *
from accounts_payable
where due_date::date < now()::date
  and payment_status = 'pending'
;

# calculate total overdue invoice amount

select 
    sum(invoice_amount) as total_overdue_amount
from accounts_payable
where due_date::date < now()::date
  and payment_status = 'pending'
;

# group invoices by vendor and calculate total amount per vendor

select 
    vendor_id,
    vendor_name,
    sum(invoice_amount) as total_invoice_amount
from accounts_payable
group by vendor_id, vendor_name
order by total_invoice_amount desc
;

# analyze payment status distribution

select 
    payment_status,
    count(*) as total_invoices,
    sum(invoice_amount) as total_amount
from accounts_payable
group by payment_status
;

