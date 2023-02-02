class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Python2
        # return num in [6, 28, 496, 8128, 33550336]
        
        # Python3 hash
        return num in {6, 28, 496, 8128, 33550336}
