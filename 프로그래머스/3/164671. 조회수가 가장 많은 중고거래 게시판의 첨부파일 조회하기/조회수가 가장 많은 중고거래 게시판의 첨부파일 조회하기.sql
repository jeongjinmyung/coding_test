with best_view as (
    select
        board_id
    from used_goods_board
    order by views desc
    limit 1
)

select
    concat(
        '/home/grep/src/',
        f.board_id, '/',
        f.file_id,
        f.file_name,
        f.file_ext
    ) as FILE_PATH
from used_goods_file f
join best_view b on f.board_id = b.board_id
order by FILE_PATH desc;
