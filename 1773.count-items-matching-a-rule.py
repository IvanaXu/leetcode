_t = {
    "type": 0,
    "color": 1,
    "name": 2,
}
class Solution:
    def countMatches(
        self, items: List[List[str]], 
        ruleKey: str, ruleValue: str
    ) -> int:
        return len([
            _items
            for _items in items
            if _items[_t.get(ruleKey)] == ruleValue
        ])
