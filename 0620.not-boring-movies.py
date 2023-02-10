SQL = """
# Write your MySQL query statement below
SELECT
    *
FROM cinema
WHERE 
    id & 1
    AND description != "boring"
ORDER BY rating DESC
"""
