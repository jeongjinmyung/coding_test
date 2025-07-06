select r.food_type, r.rest_id, r.rest_name, r.favorites
from rest_info r
where r.favorites = (
    select max(favorites)
    from rest_info
    where food_type = r.food_type
)
order by r.food_type desc;