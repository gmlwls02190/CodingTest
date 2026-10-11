-- 코드를 입력하세요
SELECT
    car_id,
    round(sum(datediff(end_date,start_date)+1)/count(*),1) as AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
having sum(datediff(end_date,start_date)+1)/count(*)>=7
order by 2 desc, 1 desc;