SQL = """
# Write your MySQL query statement below
SELECT 
    customer_id,
    count(visit_id) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id
"""
