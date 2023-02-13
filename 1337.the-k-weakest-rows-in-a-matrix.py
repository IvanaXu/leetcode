class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i["row"] for i in sorted(
            [{"row":n,"val":sum(v)} for n, v in enumerate(mat)],
            key=lambda x: (x["val"], x["row"]),
        )[:k]]
