-- 코드를 입력하세요
select
    mp.member_name,
    rr.review_text,
    rr.review_date
from member_profile as mp
join rest_review as rr
on mp.member_id=rr.member_id
where mp.member_id in (
    select
        member_id
    from rest_review
    group by member_id
    having count(*) = (
        select
            max(t1.review_count) as review_max
        from (
        select
            count(*) as review_count
        from rest_review
        group by member_id) as t1)
)
order by rr.review_date, rr.review_text;