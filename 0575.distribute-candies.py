class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # min([type numbers, half of candy])
        return min([len(candyType)//2, len(set(candyType))])
