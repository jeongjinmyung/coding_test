select ai.animal_type `ANIMAL_TYPE`,
case
    when ai.name is null
    then 'No name'
    else ai.name
    end `NAME`,
ai.sex_upon_intake `SEX_UPON_INTAKE`
from animal_ins ai
order by ai.animal_id;