from typing import List

def merge(interval: List[List[int]]) -> List[List[int]]:
    interval.sort()
    res = []
    for start, end in interval:
        if res and start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else: res.append([start,end])
    return res
print(merge([[1,3],[2,6],[15,18],[8,10]]))