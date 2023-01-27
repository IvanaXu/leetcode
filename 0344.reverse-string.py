class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for n in range(l):
            if n >= l/2:
                break
            
            s[n], s[l-n-1] = s[l-n-1], s[n]
