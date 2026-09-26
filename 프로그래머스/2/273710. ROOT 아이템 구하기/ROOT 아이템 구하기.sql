-- 코드를 작성해주세요
select
    ii.item_id as item_id,
    ii.item_name as item_name
from item_info as ii
join item_tree as it
on ii.item_id=it.item_id
where it.parent_item_id is null
order by 1;