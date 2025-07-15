with selected_user as (
    select 
        writer_id,
        sum(price) as sum_price
    from used_goods_board
    where status = 'DONE'
    group by writer_id
    having sum(price) >= 700000
)

select 
    user_id, 
    nickname,
    s.sum_price
from used_goods_user g
join selected_user s on g.user_id = s.writer_id
order by s.sum_price asc;

