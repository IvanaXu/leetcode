class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # abdda
                # (i+1,j)或(i,j-1)任意一个是回文串
                _1, _2 = s[(i+1):(j)+1], s[(i):(j-1)+1]
                return _1 == _1[::-1] or _2 == _2[::-1]
