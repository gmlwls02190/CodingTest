-- 코드를 입력하세요
SELECT
    history_id,
    car_id,
    start_date,
    end_date,
    if(datediff(end_date,start_date)>=29,'장기 대여','단기 대여') as rent_type
from car_rental_company_rental_history
where start_date like '2022-09%'
order by 1 desc;