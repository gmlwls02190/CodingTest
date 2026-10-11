-- 코드를 입력하세요
SELECT
    regexp_replace(product_code,'^(..).*','$1') as category,
    -- 앞 두글자를 추출하기 위해 ^(..)으로 앞 두글자를 괄호를 사용해서 그룹으로 묶음
    -- .*로 뒤쪽 문자를 날리고 $1로 첫번째 그룹을 가져옴
    count(*)
from product
group by 1
order by 1;