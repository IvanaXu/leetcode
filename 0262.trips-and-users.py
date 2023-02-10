SQL = """
# Write your MySQL query statement below
SELECT
    Request_at AS Day,
    ROUND(AVG(Status != 'completed'), 2) "Cancellation Rate"
FROM Trips AS T
JOIN Users AS U1 ON (T.Client_id = U1.Users_id AND U1.Banned = 'No')
JOIN Users AS U2 ON (T.Driver_id = U2.Users_id AND U2.Banned = 'No')
WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at
"""
