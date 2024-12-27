# list products below their reorder level

select 
    product_id,
    product_name,
    stock_level,
    reorder_level,
    category
from inventory_data
where stock_level < reorder_level
order by stock_level
;

# calculate total stock value for each category

select 
    category,
    sum(stock_level * price_per_unit) as total_stock_value
from inventory_data
group by category
order by total_stock_value desc
;

# identify products with zero stock level

select 
    product_id,
    product_name,
    category,
    price_per_unit
from inventory_data
where stock_level = 0
;

# calculate average price per unit by category

select 
    category,
    avg(price_per_unit) as average_price_per_unit
from inventory_data
group by category
order by average_price_per_unit desc
;
