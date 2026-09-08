class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(word, memo):
            if word in memo:
                return memo[word]
    
            if not word:
                return True

            for x in wordDict:
                if word.startswith(x):
                    if dfs(word[len(x):], memo):
                        return True
            memo[word] = False
            return memo[word]

        return dfs(s, {})