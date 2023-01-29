class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [
            i[0]
            for i in sorted(
                [(_n, _h) for _n, _h in zip(names, heights)], 
                key=lambda x: x[1], reverse=True
            )
        ]
