-- 코드를 입력하세요
select
    year(os.sales_date) as year,
    month(os.sales_date) as month,
    count(distinct os.user_id) as PURCHASED_USERS,
    round(count(distinct os.user_id)/(select count(*) from user_info where joined like "2021%"),1) as PUCHASED_RATIO
from online_sale as os
where os.user_id in (select user_id from user_info where joined like "2021%")
group by year(os.sales_date), month(os.sales_date)
order by 1, 2;