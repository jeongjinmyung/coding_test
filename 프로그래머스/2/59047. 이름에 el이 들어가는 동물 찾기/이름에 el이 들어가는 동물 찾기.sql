select ai.animal_id, ai.name
from animal_ins ai
where ai.animal_type = 'Dog' 
    and ai.name like '%EL%'
order by ai.name asc;