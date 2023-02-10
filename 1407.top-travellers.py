SQL = """
# Write your MySQL query statement below
SELECT
    U.name AS name,
    IFNULL(SUM(R.distance), 0) AS travelled_distance
FROM Users AS U
LEFT JOIN Rides AS R
ON U.id = R.user_id
GROUP BY R.user_id # SAME NAME
ORDER BY travelled_distance DESC, U.name
"""
