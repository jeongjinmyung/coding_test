select ao.animal_id, ao.name
from animal_outs as ao
left join animal_ins as ai
on ao.animal_id = ai.animal_id
where ai.datetime is null;


