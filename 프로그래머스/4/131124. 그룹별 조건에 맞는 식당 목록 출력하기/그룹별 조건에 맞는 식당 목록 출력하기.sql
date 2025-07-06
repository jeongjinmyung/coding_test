select m.member_name, r.review_text, date_format(r.review_date, "%Y-%m-%d")
from member_profile m
inner join rest_review r
    on m.member_id = r.member_id
where m.member_id = (
    select member_id
    from rest_review
    group by member_id
    order by count(*) desc
    limit 1
)
order by r.review_date asc, r.review_text asc;
