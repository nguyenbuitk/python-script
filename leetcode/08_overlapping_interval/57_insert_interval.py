from typing import List

def insert(intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
    if not intervals:
        return [newIntervals]
    res = []
    merged_new_interval = False
    if max(newIntervals) < intervals[0][0]:
        res.append(newIntervals)
        merged_new_interval = True
    for start, end in intervals:
        print(f"current res: {res}")
        if res and  min(newIntervals) > res[-1][1] and max(newIntervals) < start:
            res.append(newIntervals)
            res.append([start,end])
            merged_new_interval = True
        if res and newIntervals[0] <= end and not merged_new_interval:
            res.append([min(start,newIntervals[0]), max(end, newIntervals[1])])
            merged_new_interval = True
        elif merged_new_interval and start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
            
        else:
            if (newIntervals[0] <= end or newIntervals[0] <= start) and not merged_new_interval:
                res.append([min(start, newIntervals[0]), max(newIntervals[1], end)])
                merged_new_interval = True
            else: 
                res.append([start,end])
    if not merged_new_interval:
        res.append(newIntervals)
    return res
# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# print(insert([[1,3],[6,9]],[2,5] ))
print(insert([[1,3],[6,9]], [2,5]))
