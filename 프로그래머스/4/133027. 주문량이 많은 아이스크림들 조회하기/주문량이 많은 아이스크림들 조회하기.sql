-- 코드를 입력하세요
SELECT
    fh.flavor
from first_half as fh
join july as j
on fh.flavor=j.flavor
group by fh.flavor
order by sum(j.total_order)+sum(fh.total_order) desc
limit 3;