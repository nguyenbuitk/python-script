from typing import List
from collections import deque
def applyOperations(nums: List[int]) -> List[int]:

    dq = deque([])
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1] and nums[i] != 0:
            nums[i] *= 2
            nums[i+1] = 0
        elif nums[i] == 0:
            dq.append(i)
            continue
        if dq:
            previous_zeros = dq.popleft()
            nums[i], nums[previous_zeros] = nums[previous_zeros], nums[i]
            dq.append(i)

    if nums[-1] != 0 and dq:
         nums[-1], nums[i] = nums[i], nums[-1]
    return nums

print(applyOperations([0,1]))