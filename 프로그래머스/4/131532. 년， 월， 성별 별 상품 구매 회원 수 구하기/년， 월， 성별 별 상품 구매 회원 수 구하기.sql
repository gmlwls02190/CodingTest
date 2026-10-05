-- 코드를 입력하세요
SELECT
    year(s.sales_date) as year,
    month(s.sales_date) as month,
    f.gender,
    count(distinct f.user_id) as users
from user_info as f
right join online_sale as s
on f.user_id = s.user_id
where f.gender is not null
group by 1, 2, 3
order by 1, 2, 3;