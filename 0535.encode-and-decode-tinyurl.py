import binascii
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        _head = "http://tinyurl.com/"
        _cont = binascii.b2a_hex(longUrl.encode()).decode()
        return f"{_head}{_cont}"


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        _head = "http://tinyurl.com/"
        print(shortUrl)
        return binascii.a2b_hex(shortUrl.replace(_head, "").encode()).decode()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
