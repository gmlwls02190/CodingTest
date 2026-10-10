-- 코드를 입력하세요
SELECT
    c.car_id,
    c.car_type,
    c.daily_fee*30*(1-dp.discount_rate/100) as fee
from car_rental_company_car as c
join car_rental_company_discount_plan as dp
on c.car_type=dp.car_type
where c.car_id not in (
    select
        car_id
    from car_rental_company_rental_history
    where end_date>='2022-11-01' and start_date<='2022-11-30')
and c.car_type in ('SUV', '세단')
and dp.duration_type='30일 이상'
and c.daily_fee*30*(1-dp.discount_rate/100)>=500000
and c.daily_fee*30*(1-dp.discount_rate/100)<2000000
order by 3 desc, 2, 1 desc;