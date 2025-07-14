with jan_book as (
    select 
        book_id,
        sum(sales) as sales
    from book_sales
    where month(sales_date) = 1
    group by book_id
)

select 
    b.author_id as AUTHOR_ID,
    a.author_name as AUTHOR_NAME,
    b.category as CATEGORY,
    sum(j.sales * b.price) as TOTAL_SALES
from book b
join author a on b.author_id = a.author_id
join jan_book j on b.book_id = j.book_id
group by AUTHOR_ID, AUTHOR_NAME, CATEGORY
order by AUTHOR_ID asc, CATEGORY desc; 
