select
    car.car_type as CAR_TYPE,
    count(*) as CARS
from car_rental_company_car car
where car.options like '%통풍시트%'
    or car.options like '%열선시트%'
    or car.options like '%가죽시트%'
group by CAR_TYPE
order by CAR_TYPE asc;