-- 코드를 입력하세요
SELECT
    p.product_code as product_code,
    sum(p.price*os.sales_amount) as sales
from product as p
join offline_sale as os
on p.product_id=os.product_id
group by p.product_code
order by 2 desc, 1;