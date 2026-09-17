-- 코드를 입력하세요
SELECT
    factory_id as fi,
    factory_name,
    address
from food_factory
where address like '%강원도%'
order by fi asc;