-- 코드를 작성해주세요

select
    id,
    case ntile(4) over (order by size_of_colony desc)
    -- ntile(나누려는 그룹 갯수) over (order by 컬럼 asc/desc)
    when 1 then 'CRITICAL'
    when 2 then 'HIGH'
    when 3 then 'MEDIUM'
    else 'LOW' end as colony_name
from ecoli_data
order by id;