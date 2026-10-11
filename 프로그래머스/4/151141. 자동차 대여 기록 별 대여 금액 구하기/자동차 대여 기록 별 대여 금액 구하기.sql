-- 코드를 입력하세요
select
    h.history_id,
    case
    when datediff(end_date, start_date)+1>=90 then c.daily_fee*(datediff(end_date, start_date)+1)*(1-dp.discount_rate/100)
    when datediff(end_date, start_date)+1>=30 then c.daily_fee*(datediff(end_date, start_date)+1)*(1-dp.discount_rate/100)
    when datediff(end_date, start_date)+1>=7 then c.daily_fee*(datediff(end_date, start_date)+1)*(1-dp.discount_rate/100)
    else c.daily_fee*(datediff(end_date, start_date)+1) end as fee
from CAR_RENTAL_COMPANY_CAR as c
join (
    SELECT
        history_id,
        car_id,
        start_date,
        end_date,
        case
        when datediff(end_date, start_date)+1>=90 then '90일 이상'
        when datediff(end_date, start_date)+1>=30 then '30일 이상'
        when datediff(end_date, start_date)+1>=7 then '7일 이상'
        else null end as duration_type
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY) as h
on c.car_id=h.car_id
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as dp
on c.car_type=dp.car_type and h.duration_type=dp.duration_type
where c.car_type='트럭'
order by fee desc, 1 desc;