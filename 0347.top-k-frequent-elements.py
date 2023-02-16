class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _r = {}
        for i in nums:
            _r[i] = 1 if i not in _r else _r[i]+1
        return [
            i[0] for i in 
            sorted([[_k, _v] for _k, _v in _r.items()], key=lambda x: x[1], reverse=True)
        ][:k]
