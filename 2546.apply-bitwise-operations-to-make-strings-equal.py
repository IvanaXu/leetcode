class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """
        0,0 > 0,0: 0|0=0, 0^0=0, 
        0,1 > 1,1: 0|1=1, 0^1=1, 
        1,0 > 1,1: 1|0=1, 1^0=1, 
        1,1 > 1,0: 1|1=1, 1^1=0, 

        # 1让任意0变为1 让任意1变为0
        # 当s/t都没有1时 s/t都有1时 就返回true
        """
        return (s == target) or ("1" in s and "1" in target)
