class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _cut = max(candies) - extraCandies
        return [c >= _cut for c in candies]
