select 
    distinct h.car_id as CAR_ID
from car_rental_company_rental_history h
left join car_rental_company_car c on h.car_id = c.car_id
where c.car_type = '세단'
    and month(h.start_date) >= 10
order by CAR_ID desc;