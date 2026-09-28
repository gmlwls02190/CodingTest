-- 코드를 작성해주세요
select
    count(*) as fish_count,
    fni.fish_name as fish_name
from fish_info as fi
join fish_name_info as fni
on fi.fish_type=fni.fish_type
group by fish_name
order by fish_count desc;