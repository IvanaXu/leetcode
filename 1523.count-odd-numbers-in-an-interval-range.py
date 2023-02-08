# Python2
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high+1)/2 - low/2

# Python3
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - low//2
