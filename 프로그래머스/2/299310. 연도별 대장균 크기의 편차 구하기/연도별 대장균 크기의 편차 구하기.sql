-- 코드를 작성해주세요
select
    year(DIFFERENTIATION_DATE) as year,
    (max(size_of_colony) over(partition by year(DIFFERENTIATION_DATE)))-size_of_colony as year_dev,
    -- max(크기 컬럼)윈도우 함수 -> over(최댓값을 구할 그룹의 기준 -> partition by 그룹 컬럼 /그룹바이와 유사)
    id
from ecoli_data
order by 1,2;