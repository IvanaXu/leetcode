SQL = """
# Write your MySQL query statement below
SELECT
    S.product_id,
    P.product_name
FROM Sales AS S 
LEFT JOIN Product AS P
ON S.product_id = P.product_id
GROUP BY product_id
HAVING 
    MIN(sale_date) >= "2019-01-01" 
    AND MAX(sale_date) <= "2019-03-31"
"""
