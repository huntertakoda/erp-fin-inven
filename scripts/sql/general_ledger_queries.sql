# query to calculate net balance for each account

select 
    account_id,
    account_name,
    account_type,
    sum(debit_amount) as total_debit,
    sum(credit_amount) as total_credit,
    (sum(debit_amount) - sum(credit_amount)) as net_balance
from general_ledger
group by account_id, account_name, account_type
order by net_balance desc
;

# query to analyze transactions by account type

select 
    account_type,
    count(*) as total_transactions,
    sum(debit_amount) as total_debit,
    sum(credit_amount) as total_credit
from general_ledger
group by account_type
order by total_transactions desc
;

# query to find accounts with negative balance

select 
    account_id,
    account_name,
    (sum(debit_amount) - sum(credit_amount)) as net_balance
from general_ledger
group by account_id, account_name
having (sum(debit_amount) - sum(credit_amount)) < 0
;

# query to list transactions within a specific date range

select *
from general_ledger
where transaction_date between '2024-01-01' and '2024-12-31'
order by transaction_date
;
