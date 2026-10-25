"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        r = 0
        h = []
        intervals = sorted(intervals, key=lambda x:x.start)
        for interval in intervals:
            i,j = interval.start,interval.end
            if not h or h[0]>i:
                r+=1
            elif h[0]<=i:
                heapq.heappop(h)
            heapq.heappush(h,j)
        return r