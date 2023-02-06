# Python2
class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s1, s2 = s.split(":")
        s10, s11 = ord(s1[0]), int(s1[1])
        s20, s21 = ord(s2[0]), int(s2[1])
        
        return [
            "{0}{1}".format(chr(c), n)
            for c in range(s10, s20+1)
            for n in range(s11, s21+1)
        ]

# Python3
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s1, s2 = s.split(":")
        s10, s11 = ord(s1[0]), int(s1[1])
        s20, s21 = ord(s2[0]), int(s2[1])
        
        return [
            f"{chr(c)}{n}"
            for c in range(s10, s20+1)
            for n in range(s11, s21+1)
        ]
