"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newArr = sorted(intervals, key=lambda x: x.start)

        for x in range(len(intervals) - 1):
            if newArr[x].end > newArr[x + 1].start:
                return False;

        return True



            
