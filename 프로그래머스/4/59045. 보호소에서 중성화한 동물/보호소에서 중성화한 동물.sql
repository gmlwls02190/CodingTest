-- 코드를 입력하세요
SELECT
    ao.animal_id,
    ao.animal_type,
    ao.name
from animal_ins as ai
join animal_outs as ao
on ai.animal_id=ao.animal_id
where ai.sex_upon_intake like "intact%" and ao.sex_upon_outcome regexp "^[neutered|spayed]"
order by 1;