class TrieNode:
    def __init__(self):
        self.chars = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.start = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.start


        for char in word:
            if char not in curr.chars:
                curr.chars[char] = TrieNode()

            curr = curr.chars[char]

        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.start

        for c in word:
            if c not in curr.chars:
                return False

            curr = curr.chars[c]

        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.start

        for c in prefix:
            if c not in curr.chars:
                return False

            curr = curr.chars[c]

        return True
        
        