WITH l as (
    SELECT *,
    LAG(num, 1) OVER (ORDER BY id) as first_num,
    LAG(num, 2) OVER (ORDER BY id) as second_num
    FROM Logs 
)

select distinct num as ConsecutiveNums
FROM l
WHERE num = first_num AND num = second_num