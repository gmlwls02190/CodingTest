-- 코드를 입력하세요
SELECT
    u.user_id,
    u.nickname,
    concat_ws(' ', u.city, u.street_address1, u.street_address2) as 전체주소,
    regexp_replace(u.tlno, '^([0-9]{3})([0-9]{4})([0-9]{4})', '$1-$2-$3') as 전화번호
from used_goods_board as b
join used_goods_user as u
on b.writer_id=u.user_id
group by u.user_id
having count(u.user_id)>=3
order by 1 desc;