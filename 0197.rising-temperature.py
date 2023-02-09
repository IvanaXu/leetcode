SQL = """
# Write your MySQL query statement below
select id 
from (
    select 
        id, 
        recordDate as RD, 
        Temperature as TR, 
        lag(recordDate) over(order by recordDate) lRD, 
        lag(Temperature) over(order by recordDate) lTR
    from Weather
) T
where T.TR > T.lTR and dateDiff(T.RD, T.lRD) = 1
"""
