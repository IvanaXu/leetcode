class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = sorted(gifts)
        for _ in range(k):
            gifts = sorted(gifts)
            gifts[-1] = int(math.sqrt(gifts[-1]))
        return sum(gifts)
