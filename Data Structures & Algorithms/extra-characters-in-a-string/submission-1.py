class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        res = float('inf')
        memo = {}

        def dfs(curr, extra=0):
            nonlocal res
            res = min(res, extra + len(curr))

            if not curr:
                return

            if curr in memo and memo[curr] <= extra:
                return

            memo[curr] = extra

            for x in dictionary:
                if curr.startswith(x):
                    dfs(curr[len(x):], extra)

            dfs(curr[1:], extra + 1)

        dfs(s)
        return res