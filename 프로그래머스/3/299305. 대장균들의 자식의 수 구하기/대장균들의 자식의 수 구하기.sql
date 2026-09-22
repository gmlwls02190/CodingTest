-- 코드를 작성해주세요
select
    pd.id as id,
    ifnull(count(cd.id),0) as child_count
from ecoli_data as pd
left join ecoli_data as cd
on pd.id=cd.parent_id
group by pd.id
order by pd.id;