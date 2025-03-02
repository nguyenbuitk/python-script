
from collections import deque
from typing import List
def transformArray(nums: List[int]) -> List[int]:
    dq = deque([])
    for i in range(len(nums)):
        if nums[i]%2 == 1:
            nums[i] = 1
            dq.append(i)
        else:
            nums[i] = 0
            if dq:
                j = dq.popleft()
                nums[i], nums[j] = nums[j], nums[i]
                dq.append(i)
    return nums

print(transformArray([21,10,24]))
print(transformArray([21,10,24]))