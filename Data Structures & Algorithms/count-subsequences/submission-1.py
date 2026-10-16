class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        def dfs(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if s[i] == t[j]:
                
                memo[(i, j)] = dfs(i + 1, j + 1, memo) + dfs(i + 1, j, memo)
                return memo[(i, j)]

            memo[(i, j)] = dfs(i + 1, j, memo)
            return memo[(i, j)]

        return dfs(0, 0, {})
            


            
        