from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort()
    print(intervals)
    count = 0
    current_interval = []
    for start, end in intervals:
        if current_interval and start < current_interval[1]:
            count += 1
            if end < current_interval[1]:
                current_interval = [start,end]
        else:
            current_interval = [start, end]
            print(f"current_interval: {current_interval}")
            print(f"current_count = {count}")
    return count 
    
eraseOverlapIntervals( [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
