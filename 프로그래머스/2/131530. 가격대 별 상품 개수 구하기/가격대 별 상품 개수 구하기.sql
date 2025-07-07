select
case
    when length(price) < 5
    then '0'
    else concat(left(price, 1), '0000')
    end as 'price_group',
count('price_group') `products`
from product
group by price_group
order by price_group asc;
