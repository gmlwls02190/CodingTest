-- 코드를 작성해주세요
select
    ii.item_id as item_id,
    ii.item_name as item_name,
    ii.rarity as rarity
from item_info as ii
left join item_tree as it
on ii.item_id=it.parent_item_id
where it.item_id is null
order by 1 desc;