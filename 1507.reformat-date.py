class Solution:
    def reformatDate(self, date: str) -> str:
        _m = {
            "Jan": "01", "Feb": "02", "Mar": "03", 
            "Apr": "04", "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", "Sep": "09", 
            "Oct": "10", "Nov": "11", "Dec": "12",
        }
        d, m, y = date.split(" ")
        return f"{y}-{_m.get(m)}-{('0'+d if len(d) == 3 else d)[:2]}"
