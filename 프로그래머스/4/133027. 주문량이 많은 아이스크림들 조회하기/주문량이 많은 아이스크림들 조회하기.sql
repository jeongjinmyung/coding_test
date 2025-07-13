with july_total as (
    select flavor, sum(total_order) as TOTAL_ORDER
    from july
    group by flavor
)

select f.flavor
from first_half f
join july_total j on f.flavor = j.flavor
order by (f.total_order + j.total_order) desc
limit 3;