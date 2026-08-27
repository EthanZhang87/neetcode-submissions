class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()
        

    def insert(self, word: str) -> None:
        start = self.head

        for c in word:
            if c not in start.children:
                start.children[c] = TrieNode()

            start = start.children[c]

        start.endOfWord = True

        


    def search(self, word: str) -> bool:
        start = self.head

        for c in word:
            if c not in start.children:
                return False
            start = start.children[c]

        return start.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        start = self.head

        for c in prefix:
            if c not in start.children:
                return False

            start = start.children[c]

        return True
        
        