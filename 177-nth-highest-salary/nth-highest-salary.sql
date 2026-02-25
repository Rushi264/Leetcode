CREATE OR REPLACE FUNCTION NthHighestSalary(N INT)
RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY
    SELECT MAX(t.salary) AS Salary
    FROM (
      SELECT e.salary,
             DENSE_RANK() OVER (ORDER BY e.salary DESC) AS rnk
      FROM Employee e
    ) t
    WHERE t.rnk = N;
END;
$$ LANGUAGE plpgsql;