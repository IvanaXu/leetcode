SQL = """
# Write your MySQL query statement below
SELECT
    DISTINCT(L1.Num) AS ConsecutiveNums
FROM
    Logs AS L1,
    Logs AS L2,
    Logs AS L3
WHERE
    L1.Id + 1 = L2.Id
    AND L2.Id + 1 = L3.Id
    AND L1.Num = L2.Num
    AND L2.Num = L3.Num
"""
