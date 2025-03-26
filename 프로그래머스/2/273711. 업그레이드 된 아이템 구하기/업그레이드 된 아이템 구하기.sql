select I.item_id, I.item_name, I.rarity
from item_info I
inner join item_tree T
    on I.item_id = T.item_id
where T.parent_item_id in (
    select item_id
    from item_info
    where rarity = 'RARE'
)
order by I.item_id desc;