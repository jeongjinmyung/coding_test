select id, email, first_name, last_name
from developer_infos
where skill_1 = 'Python'
    or skill_2 = 'Python'
    or skill_3 = 'python'
order by id asc;