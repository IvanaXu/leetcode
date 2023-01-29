class Solution:
    def countLargestGroup(self, n: int) -> int:
        _r = {}
        for i in range(1, n+1):
            v = sum([int(j) for j in str(i)])
            if v in _r:
                _r[v] += 1
            else:
                _r[v] = 0
        
        _r = list(_r.values())
        _max = max(_r)
        return sum([i == _max for i in _r])
