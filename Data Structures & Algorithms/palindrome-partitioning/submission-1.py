class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(val):
            return len(val) > 0 and val == val[::-1]


        def dfs(i, curr):
            if i == len(s):
                res.append(curr.copy())
                return

            for x in range(i, len(s)):
                substring = s[i:x + 1]

                if isPalindrome(substring):
                    curr.append(substring)
                    dfs(x + 1, curr)
                    curr.pop()

            return

        dfs(0, [])

        return res

        