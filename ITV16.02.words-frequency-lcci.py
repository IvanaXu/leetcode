class WordsFrequency:

    def __init__(self, book: List[str]):
        self._r = {}
        for i in book:
            if i not in self._r:
                self._r[i] = 1
            else:
                self._r[i] += 1

    def get(self, word: str) -> int:
        return self._r.get(word, 0)

# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
