SQL = """
# Write your MySQL query statement below
# SELECT DISTINCT salary AS SecondHighestSalary
#     FROM Employee 
#     ORDER BY salary DESC 
#     LIMIT 1, 1
# {"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100]]}}
# {"headers":["SecondHighestSalary"],"values":[[null]]}
# BUT, {"headers": ["SecondHighestSalary"], "values": []}

SELECT (
    SELECT DISTINCT salary
    FROM Employee 
    ORDER BY salary DESC 
    LIMIT 1, 1
) AS SecondHighestSalary
# 
"""
