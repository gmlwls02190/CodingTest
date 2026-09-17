-- 코드를 입력하세요
SELECT
    book_id as '도서 ID',
    published_date as 출판일
from book
where year(published_date)='2021' and category = '인문'
order by published_date asc; 