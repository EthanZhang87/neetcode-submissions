class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        res = -1


        for k, v in enumerate(s):
            if v in seen:
                res = max(res, k - seen[v] - 1)
            else:
                seen[v] = k

        return res


        