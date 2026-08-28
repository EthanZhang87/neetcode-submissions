"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        curr = []

        for x in intervals:
            curr.append((x.start, "S"))
            curr.append((x.end, 'E'))

        curr.sort(key = lambda x: (x[0], x[1]))
        res = 0
        total = 0
        for x in curr:
            if x[1] == 'S':
                total += 1
                res = max(res, total)
            elif x[1] == 'E':
                total -= 1
                res = max(res, total)

        return res
        