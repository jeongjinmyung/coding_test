select substring(product_code, 1, 2) `category`, count('category') `products`
from product
group by category
order by category asc;
