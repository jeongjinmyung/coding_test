select fp.product_id, fp.product_name,
    sum(fp.price * fo.amount) as `TOTAL_SALES`
from food_product fp
inner join food_order fo
    on fp.product_id = fo.product_id
where year(fo.produce_date) = '2022'
    and month(fo.produce_date) = '05'
group by fp.product_name
order by `TOTAL_SALES` desc, fp.product_id asc;