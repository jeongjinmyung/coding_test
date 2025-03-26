select D.id, D.email, D.first_name, D.last_name
from developers as D
where (D.skill_code & (select sum(S.code)
                    from skillcodes as S
                    where S.name in ('Python', 'C#'))
       ) > 0
order by D.id asc;