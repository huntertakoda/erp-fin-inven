# create a role for read-only users

create role read_only_user
;

# grant select permissions to read-only users on all tables

grant select on general_ledger to read_only_user
;

grant select on accounts_payable to read_only_user
;

grant select on fixed_assets to read_only_user
;

grant select on inventory_data to read_only_user
;


# create a role for data analysts with additional permissions

create role data_analyst
;

# grant select and insert permissions to data analysts on specific tables

grant select, insert on general_ledger to data_analyst
;

grant select, insert on accounts_payable to data_analyst
;

grant select, insert on fixed_assets to data_analyst
;

# create a role for administrators with full access

create role admin_role
;

# grant all privileges to administrators on all tables

grant all privileges on all tables in schema public to admin_role
;

# create specific users and assign roles

create user read_user with password 'readpassword'
;

grant read_only_user to read_user
;

create user analyst_user with password 'analystpassword'
;

grant data_analyst to analyst_user
;

create user admin_user with password 'adminpassword'
;

grant admin_role to admin_user
;
