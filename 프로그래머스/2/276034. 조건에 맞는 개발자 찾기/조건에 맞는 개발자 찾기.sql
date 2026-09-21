-- 코드를 작성해주세요
select
    distinct d.id, -- 한 개발자가 두가지 기술을 다 가지고 있을 경우 중복을 제거
    d.email,
    d.first_name,
    d.last_name
from skillcodes as s
join developers as d
on (s.code & d.skill_code)=s.code -- 비트 연산자 &(AND)를 사용
where s.name in ('Python', 'C#')
order by d.id;