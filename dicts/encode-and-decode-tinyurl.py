class Codec:
    '''
        https://leetcode.com/problems/encode-and-decode-tinyurl/description/
    '''
    def __init__(self):
        self.store = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.store:
            shortUrl = "http://tinyurl.com/"+ str(len(self.store)+1)
            self.store[longUrl] = shortUrl
            self.store[shortUrl] = longUrl

        return self.store[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))