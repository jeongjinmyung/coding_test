select hour(ao.datetime) as `HOUR`, count(*) as `COUNT`
from animal_outs ao
group by `HOUR`
    having `HOUR` >= 9 and `HOUR` < 20
order by `HOUR` asc;