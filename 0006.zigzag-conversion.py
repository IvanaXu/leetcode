class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows-2
        m = numRows + n
        l, r = "", {}
        
        if n >= 0:
            pass
        else:
            return s
        
        for j in range(numRows):
            r[j] = ""
        
        for i in range(len(s)//m+1):
            si = s[m*i:m*(i+1)]
            if si:
                si1, si2 = si[:numRows], si[numRows:]
                for j in range(numRows):
                    if j in [0, numRows-1]:
                        r[j] = r[j] + (si1[j] if j < len(si1) else "")
                    else:
                        r[j] = r[j] + (si1[j] if j < len(si1) else "") + (si2[n-j] if n-j < len(si2) else "")
        for i in r.values():
            l += i
        return l
