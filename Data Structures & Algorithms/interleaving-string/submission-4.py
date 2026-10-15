class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs (i, j, memo):
            if i + j == len(s3):
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s1) and s3[i + j] == s1[i]:
                memo[(i, j)] = dfs(i + 1, j, memo)
                if memo[(i, j)]:
                    return memo[(i, j)]
            
            if j < len(s2) and s3[i + j] == s2[j]:
                memo[(i, j)] = dfs(i, j + 1, memo)
                if memo[(i, j)]:
                    return memo[(i, j)]

            memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0, {})

            
            
