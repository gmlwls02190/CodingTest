-- 코드를 작성해주세요
select
    c.id as id
from ecoli_data as a
join ecoli_data as b
on a.id=b.parent_id
join ecoli_data as c
on b.id=c.parent_id
where a.parent_id is null
order by c.id;