# Python2
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return longUrl[::-1]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return shortUrl[::-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# Python3
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
