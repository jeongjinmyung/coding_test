with history as (
    select
        car_id
    from car_rental_company_rental_history
    where start_date >= '2022-08-01' and start_date < '2022-11-01'
    group by car_id
    having count(*) >= 5    
)

select
    month(car.start_date) as MONTH,
    car.car_id as CAR_ID,
    count(*) as RECORDS
from car_rental_company_rental_history as car
join history on car.car_id = history.car_id
where car.start_date >= '2022-08-01' and car.start_date < '2022-11-01'
group by MONTH, CAR_ID
order by MONTH asc, CAR_ID desc;
