SQL = """
# Write your MySQL query statement below
SELECT 
    score, 
    dense_rank() OVER(ORDER BY score desc) 'rank'
FROM Scores
"""
