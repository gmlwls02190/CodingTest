-- 코드를 입력하세요
with recursive hours as(
    select 0 as hour
    union all
    select hour+1 from hours where hour < 23)

SELECT
    h.hour,
    count(o.animal_id) as count
from animal_outs as o
right join hours as h
on hour(o.datetime) = h.hour
group by h.hour;