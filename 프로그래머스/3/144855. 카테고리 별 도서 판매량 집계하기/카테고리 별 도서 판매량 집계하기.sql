with jan_book as (
    select 
        book_id, 
        sum(sales) as total
    from book_sales
    where month(sales_date) = '1'
    group by book_id
)

select 
    book.category as CATEGORY,
    sum(jan_book.total) as TOTAL_SALES
from book
join jan_book on book.book_id = jan_book.book_id
group by CATEGORY
order by CATEGORY asc;