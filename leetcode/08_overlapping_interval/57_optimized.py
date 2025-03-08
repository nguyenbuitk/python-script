from typing import List

def insert(intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
    if not intervals:
        return [newIntervals]
    res = []
    intervals2 = []
    merged = False
    for index, interval in enumerate(intervals):
        if interval[0] > newIntervals[0]:
            intervals2 = intervals[:index] + [newIntervals] + intervals[index:]
            merged = True
            break
    if not merged:
        intervals2 = intervals + newIntervals
    print(intervals2)
    for start, end in intervals2[1:]:
        if res and start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else: res.append([start,end])
    
    return res 
# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# print(insert([[1,3],[6,9]],[2,5] ))
print(insert([[1,3],[6,9]], [2,5]))
