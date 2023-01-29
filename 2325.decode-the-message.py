class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        secret, c, n = {}, "abcdefghijklmnopqrstuvwxyz", 0
        for k in key.replace(" ", ""):
            if k not in secret:
                secret[k] = c[n]
                n += 1
        return "".join([secret.get(i, " ") for i in message])
