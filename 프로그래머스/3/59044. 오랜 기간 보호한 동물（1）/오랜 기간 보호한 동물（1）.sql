-- 코드를 입력하세요
select
    ins.name,
    ins.datetime
from animal_ins as ins, (
    SELECT
        ai.animal_id,
        ai.name,
        ai.datetime
    from animal_ins as ai
    left join animal_outs as ao
    on ai.animal_id=ao.animal_id
    where ao.animal_id is null
    order by ai.datetime
    limit 3) as t
where ins.animal_id=t.animal_id
order by ins.datetime;