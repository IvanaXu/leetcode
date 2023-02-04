class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        _s, _r = "", True
        _sentence = sentence.split(" ")
        _sentence += [_sentence[0]]

        for n, v in enumerate(_sentence):
            if n == 0:
                _s = v
            else:
                _r = _r and (_s[-1] == v[0])
                _s = v
        return _r
