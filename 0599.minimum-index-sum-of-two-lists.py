class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        _r = {
            x: list1.index(x)+list2.index(x)
            for x in (set(list1) & set(list2))
        }
        _min = min(_r.values())
        return [_k for _k, _v in _r.items() if _v == _min]
