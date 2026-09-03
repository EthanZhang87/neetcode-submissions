class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for x in s:
            counts[x] = counts.get(x, 0) + 1

        res = []
        l = 0
        visiting = set()
        for r in range(len(s)):
            if s[r] not in visiting:
                visiting.add(s[r])

            counts[s[r]] -= 1
            if counts[s[r]] == 0:
                visiting.remove(s[r])

            if len(visiting) == 0:
                res.append(r - l + 1)
                l = r + 1

        return res
                

