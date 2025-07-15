with selected_user as (
    select
        writer_id
    from used_goods_board
    group by writer_id
    having count(*) >= 3
)

select
    g.user_id,
    g.nickname,
    concat(g.city, ' ', g.street_address1, ' ', g.street_address2) as 전체주소,
    concat(left(g.tlno, 3), '-', substring(g.tlno, 4, 4), '-', right(g.tlno, 4)) as 전화번호
from used_goods_user g
join selected_user s on g.user_id = s.writer_id
order by g.user_id desc;