SQL = """
# Write your MySQL query statement below
SELECT 
    D.name AS Department,
    E.name AS Employee,
    Salary 
FROM 
    Employee AS E
JOIN Department AS D
ON E.departmentId = D.id
WHERE salary IN (
	SELECT salary
	FROM (
		SELECT DISTINCT salary
		FROM employee AS T1
		WHERE E.departmentId = T1.departmentId
		ORDER BY salary desc
		LIMIT 3
	) AS T2
)
"""
