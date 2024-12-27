# calculate total acquisition cost and depreciation

select 
    sum(acquisition_cost) as total_acquisition_cost,
    sum(acquisition_cost * (depreciation_rate / 100)) as total_depreciation
from fixed_assets
;

# list assets nearing the end of their lifespan

select 
    asset_id,
    asset_name,
    asset_type,
    lifespan_years,
    purchase_date
from fixed_assets
where lifespan_years <= 2
order by lifespan_years
;

# group assets by type and calculate total acquisition cost per type

select 
    asset_type,
    count(*) as total_assets,
    sum(acquisition_cost) as total_acquisition_cost
from fixed_assets
group by asset_type
order by total_acquisition_cost desc
;

# analyze average depreciation rate by asset type

select 
    asset_type,
    avg(depreciation_rate) as average_depreciation_rate
from fixed_assets
group by asset_type
order by average_depreciation_rate desc
;
