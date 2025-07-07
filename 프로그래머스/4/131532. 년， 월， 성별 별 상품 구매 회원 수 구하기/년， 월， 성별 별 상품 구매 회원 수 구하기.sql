select 
    date_format(o.sales_date, '%Y') `year`, 
    date_format(o.sales_date, '%m') `month`,
    u.gender,
    count(distinct u.user_id) `users`
from online_sale o
join user_info u on o.user_id = u.user_id
where u.gender is not null
group by year, month, u.gender
order by year asc, month asc, u.gender asc; 
