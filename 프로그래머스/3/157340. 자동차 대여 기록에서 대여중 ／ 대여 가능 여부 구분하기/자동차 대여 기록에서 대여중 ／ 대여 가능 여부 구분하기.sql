SELECT 
    car_id,
    CASE 
        WHEN '2022-10-16' BETWEEN start_date AND end_date
        THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM car_rental_company_rental_history
WHERE '2022-10-16' BETWEEN start_date AND end_date
   OR car_id NOT IN (
       SELECT car_id
       FROM car_rental_company_rental_history
       WHERE '2022-10-16' BETWEEN start_date AND end_date
   )
GROUP BY car_id
ORDER BY car_id DESC;
