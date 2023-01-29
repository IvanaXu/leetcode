class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        _arr, _l = arr, len(arr)
        for i in range(_l):
            for j in range(_l):
                if i != j and _arr[i] == _arr[j] * 2:
                    return True
        return False
