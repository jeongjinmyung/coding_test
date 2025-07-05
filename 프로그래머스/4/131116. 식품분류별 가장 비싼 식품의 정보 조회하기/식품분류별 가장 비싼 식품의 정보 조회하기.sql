select f.category, f.price, f.product_name
from food_product f
where f.category in ('과자', '국', '김치', '식용유')
and price = (
    select max(price)
    from food_product
    where category = f.category
)
order by f.price desc;