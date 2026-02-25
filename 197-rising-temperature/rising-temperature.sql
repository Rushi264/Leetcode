WITH w AS (
    SELECT  id, 
    recordDate,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate ) AS prev_temp,
    LAG(recordDate) OVER (ORDER BY recordDate ) AS prev_date
    FROM Weather
)

select id
from w
where recordDate = prev_date + INTERVAL '1 day'
    AND temperature > prev_temp