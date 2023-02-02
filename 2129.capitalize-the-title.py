class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([
            f"{i[0] if len(i) < 3 else i[0].upper()}{i[1:]}" 
            for i in title.lower().split(" ")
        ])
