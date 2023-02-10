SQL = """
# Write your MySQL query statement below
SELECT
    D.name AS Department,
    E.name AS Employee,
    E.Salary AS Salary
FROM Employee AS E, Department AS D
WHERE 
    E.departmentId = D.id
    AND (E.departmentId, E.salary) IN (
        SELECT 
            departmentId, 
            MAX(salary) AS salary
        FROM Employee
        GROUP BY departmentId
    )
"""
