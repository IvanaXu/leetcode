SQL = """
# Write your MySQL query statement below
SELECT
    T._ID AS id,
    CASE WHEN MAX(T._PID) IS NULL THEN "Root" 
    ELSE (
        CASE WHEN MAX(T._CID) IS NULL THEN "Leaf" ELSE "Inner" END
    ) END AS Type
FROM (
    SELECT
        T1.id AS _ID,
        T1.p_id AS _PID,
        T2.id AS _CID
    FROM tree AS T1
    LEFT JOIN tree AS T2
    ON T1.id = T2.p_id
) AS T
GROUP BY T._ID
"""
