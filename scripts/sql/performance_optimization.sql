# create indexes to speed up queries on general ledger

create index if not exists idx_general_ledger_account_id
on general_ledger (account_id)
;

create index if not exists idx_general_ledger_transaction_date
on general_ledger (transaction_date)
;

# create indexes to optimize overdue invoice queries in accounts payable

create index if not exists idx_accounts_payable_due_date
on accounts_payable (due_date)
;

create index if not exists idx_accounts_payable_payment_status
on accounts_payable (payment_status)
;

# create indexes to optimize fixed assets queries by type

create index if not exists idx_fixed_assets_asset_type
on fixed_assets (asset_type)
;

# optimize inventory management queries by category and stock level

create index if not exists idx_inventory_data_category
on inventory_data (category)
;

create index if not exists idx_inventory_data_stock_level
on inventory_data (stock_level)
;

# analyze table statistics for better query planning

analyze general_ledger
;

analyze accounts_payable
;

analyze fixed_assets
;

analyze inventory_data
;

