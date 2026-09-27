-- 코드를 입력하세요
SELECT
    car_type,
    count(*) as cars
from car_rental_company_car
where options regexp '[통풍|열선|가죽]시트'
group by 1
order by 1;