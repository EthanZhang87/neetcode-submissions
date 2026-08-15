class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = strs[0]
        ans, length = '', float('inf')


        for x in range(1, len(strs)):
            curr = 0
            for y in range(min(len(res), len(strs[x]))):
                if res[y] != strs[x][y]:
                    break
                if res[y] == strs[x][y]:
                    curr += 1

            if curr < length:
                length = curr
                ans = res[0:curr]


        return ans

