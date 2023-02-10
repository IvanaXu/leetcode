SQL = """
# Write your MySQL query statement below
SELECT DISTINCT A.* 
FROM 
    stadium AS A,
    stadium AS B,
    stadium AS C
WHERE 
    A.people >= 100 
    AND B.people >= 100 
    AND C.people >= 100
AND (
    # C B A 
     (A.id = B.id-1 AND B.id = C.id-1)
    # B A C 
     OR (A.id = B.id-1 AND A.id = C.id+1)
    # A B C
     OR (A.id = B.id+1 AND B.id = C.id+1)
)
ORDER BY a.id
"""
