from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]):
    res, i , n = [], 0, len(intervals)
    
    # step 1: add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    
    # step 2: currently, we know that next element will be overlapping
    # so merge overlapping intervals with newInterval until it is non overlapping
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    res.append(newInterval)

    # step 3: add non-overlapping intervals
    while i < n:
        res.append(intervals[i])
        i += 1
    return res
    
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(insert([[1,3],[6,9]],[2,5] ))
print(insert([[1,5]],[0,0] ))
print(insert([[1,5], [6,9]],[15,20] ))
