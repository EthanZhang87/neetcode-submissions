class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        intervals.append(newInterval)

        intervals.sort(key = lambda x: x[0])


        for start, end in intervals:
            if res and start <= res[-1][1] and end >= res[-1][0]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])


        return res
            