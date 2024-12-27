# calculate average monthly sales for inventory forecasting

select 
    product_id,
    product_name,
    category,
    avg(sales_quantity) as avg_monthly_sales
from sales_data
group by product_id, product_name, category
order by avg_monthly_sales desc
;

# predict stock depletion date based on current stock and sales rate

select 
    product_id,
    product_name,
    category,
    stock_level,
    avg_monthly_sales,
    case 
        when avg_monthly_sales = 0 then null
        else current_date + (stock_level / avg_monthly_sales) * interval '1 month'
    end as projected_depletion_date
from (
    select 
        product_id,
        product_name,
        category,
        stock_level,
        avg(sales_quantity) as avg_monthly_sales
    from sales_data
    join inventory_data using (product_id)
    group by product_id, product_name, category, stock_level
) as forecast
order by projected_depletion_date
;

# identify products at risk of stockouts within the next 30 days

select 
    product_id,
    product_name,
    category,
    stock_level,
    projected_depletion_date
from (
    select 
        product_id,
        product_name,
        category,
        stock_level,
        case 
            when avg_monthly_sales = 0 then null
            else current_date + (stock_level / avg_monthly_sales) * interval '1 month'
        end as projected_depletion_date
    from (
        select 
            product_id,
            product_name,
            category,
            stock_level,
            avg(sales_quantity) as avg_monthly_sales
        from sales_data
        join inventory_data using (product_id)
        group by product_id, product_name, category, stock_level
    ) as forecast
) as risk
where projected_depletion_date <= current_date + interval '30 days'
order by projected_depletion_date
;
