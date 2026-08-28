class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.characters = {}

class WordDictionary:

    def __init__(self):
        self.start = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.start
        for c in word:
            if c not in curr.characters:
                curr.characters[c] = TrieNode()
            
            curr = curr.characters[c]

        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for x in range(i, len(word)):
                if word[x] == '.':
                    for val in curr.characters.values():
                        if dfs(x + 1, val):
                            return True

                    return False

                else:
                    if word[x] not in curr.characters:
                        return False
                    curr = curr.characters[word[x]]

            return curr.isEndOfWord

        return dfs(0, self.start)                
        
