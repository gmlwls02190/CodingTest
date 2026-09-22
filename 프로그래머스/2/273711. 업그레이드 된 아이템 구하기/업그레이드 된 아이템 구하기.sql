-- 코드를 작성해주세요
select
    binfo.item_id as item_id,
    binfo.item_name as item_name,
    binfo.rarity as rarity
from item_tree as tree
join item_info as ainfo
on tree.parent_item_id=ainfo.item_id
join item_info as binfo
on tree.item_id=binfo.item_id
where ainfo.rarity='RARE'
order by binfo.item_id desc;