class Solution:
    def countTime(self, time: str) -> int:
        [h0, h1, _, m0, m1] = [t == "?" for t in time]
        k1, k2 = 1, 1
        if h0:
            if h1:
                k1 = 24
            elif time[1] <= "3":
                k1 = 3
            elif time[1] > "3":
                k1 = 2
        elif h1:
            if time[0] < "2":
                k1 = 10
            elif time[0] == "2":
                k1 = 4
        
        if m0:
            k2 = 60 if m1 else 6
        elif m1:
            k2 = 10
        
        return k1 * k2
