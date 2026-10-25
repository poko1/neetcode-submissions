"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        intervals = sorted(intervals,key=lambda x:x.start)
        pi,pj = intervals[0].start,intervals[0].end
        for interval in intervals[1:]:
            i,j = interval.start, interval.end
            if pi==i or i<pj:
                return False
            pi = i
            pj = j
        return True
