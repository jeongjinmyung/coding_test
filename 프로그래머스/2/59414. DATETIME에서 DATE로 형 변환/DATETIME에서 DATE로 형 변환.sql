select ai.animal_id `ANIMAL_ID`, ai.name `NAME`, date_format(ai.datetime, "%Y-%m-%d") `날짜`
from animal_ins ai
order by ai.animal_id;

