-- 코드를 입력하세요
SELECT
    a.author_id as author_id,
    a.author_name as author_name,
    b.category as category,
    sum(bs.sales*b.price) as sales
from book_sales as bs
join book as b
on bs.book_id=b.book_id
join author as a
on b.author_id=a.author_id
where sales_date like '2022-01%'
group by a.author_id, b.category
order by 1,3 desc;