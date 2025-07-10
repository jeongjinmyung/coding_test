select DATE_Format(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
        product_id,
        user_id,
        sales_amount
from online_sale
where month(sales_date) = 3

union

select DATE_Format(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
        product_id,
        null as `user_id`,
        sales_amount
from offline_sale
where month(sales_date) = 3

order by sales_date, product_id, user_id;
