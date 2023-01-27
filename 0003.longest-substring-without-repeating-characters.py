class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        j, m = "", 0
        for i in s:
            if i in j:
                j = j[j.index(i)+1:]
            j += i
            m = max(m, len(j))
        return m
