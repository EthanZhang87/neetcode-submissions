class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = float('inf')
        ans = [0, 0]
        count = Counter(t)
        have, need = 0, len(count)


        curr = {}
        l = 0

        for r in range(len(s)):
            if s[r] in count:
                curr[s[r]] = curr.get(s[r], 0) + 1

                if curr[s[r]] == count[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) < res:
                    res = r - l + 1
                    ans[0] = l
                    ans[1] = r + 1

                if s[l] in count:
                    curr[s[l]] -= 1

                    if curr[s[l]] < count[s[l]]:
                        have -= 1

                l += 1

        return s[ans[0]:ans[1]]

            



        
        