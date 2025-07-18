select distinct cp.cart_id `CART_ID`
from cart_products cp
where cp.cart_id in (
    select cart_id
    from cart_products
    where name in ("Milk", "Yogurt")
    group by cart_id
    having count(distinct name) = 2 # 두 개를 동시에 구입
)
order by cp.cart_id;
