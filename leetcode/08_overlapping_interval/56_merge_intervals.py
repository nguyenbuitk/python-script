from typing import List

def merge(interval: List[List[int]]) -> List[List[int]]:
    interval.sort()
    res = [interval[0]]
    for start, end in interval[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else: res.append([start,end])
    return res    
merge([[1,3],[2,6],[15,18],[8,10]])
