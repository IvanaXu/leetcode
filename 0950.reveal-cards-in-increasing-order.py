class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 逆序完成
        _l, deck = len(deck), sorted(deck, reverse=True)
        _r = []
        for i in range(_l):
            v = deck[i]
            if i == 0:
                _r = [v]
            else:
                _r.insert(0, _r.pop(-1))
                _r.insert(0, v)
        return _r
