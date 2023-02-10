SQL = """
# Write your MySQL query statement below

# SELECT 
#     FirstName,
#     LastName,
#     City,
#     State
# FROM Person AS P, Address AS A
# WHERE P.PersonId = A.PersonId
# # [["Bob", "Alice", "New York City", "New York"]]

SELECT 
    FirstName,
    LastName,
    City,
    State
FROM Person AS P
LEFT JOIN Address AS A
ON P.PersonId = A.PersonId
# [["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]

"""
