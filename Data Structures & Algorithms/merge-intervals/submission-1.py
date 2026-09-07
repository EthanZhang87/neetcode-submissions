class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []

        for start, end in intervals:
            if res and res[-1][0] <= end and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
                res[-1][0] = min(res[-1][0], start)

            else:
                res.append([start, end])

        return res

