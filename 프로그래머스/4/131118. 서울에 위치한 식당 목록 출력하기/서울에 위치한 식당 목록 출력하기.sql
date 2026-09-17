-- 코드를 입력하세요
SELECT
    ri.rest_id,
    ri.rest_name,
    ri.food_type,
    ri.favorites,
    ri.address,
    round(avg(rr.review_score),2)
from rest_info as ri
join rest_review as rr
on ri.rest_id=rr.rest_id
where ri.address like '서울%'
group by ri.rest_id
order by round(avg(rr.review_score),2) desc, ri.favorites desc;