-- 코드를 작성해주세요
select
    case
    when sum(case when s.category='front end' then 1 else 0 end)>0
            -- group by 되어 겹쳐진 데이터들을 각각 확인하기 위해서 sum()안에 case end를 사용
            and sum(case when s.name='Python' then 1 else 0 end)>0 then 'A'
    when sum(case when s.name='C#' then 1 else 0 end)>0 then 'B'
    when sum(case when s.category='front end' then 1 else 0 end)>0 then 'C'
    end as grade,
    d.id,
    d.email
from developers as d
join skillcodes as s
on d.skill_code&s.code
group by 2,3
having grade is not null
order by 1, 2;

