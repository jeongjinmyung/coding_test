select *
from places p
where p.host_id in (
    select host_id
    from places
    group by host_id
    having count(host_id) >= 2
)
order by p.id asc;


