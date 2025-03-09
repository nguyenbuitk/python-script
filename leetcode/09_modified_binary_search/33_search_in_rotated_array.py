from typing import List
import time
def search(nums: list[int], target: int) -> int:
    # Step 1: find the pivot, mark it as mid
    l, r = 0, len(nums) - 1
    offset = None
    while l < r:
        mid = (l+r)//2
        if nums[mid] > nums[l] and nums[mid] > nums[r]:
            l = mid 
        elif nums[mid] < nums[r] and nums[mid] < nums[l]:
            r = mid
        else:
            break
    print(f"mid 1: {mid}")
    if nums[mid] < nums[mid+1]:
        res = nums.copy()
        offset = 0
    else: res = nums[mid+1:] + nums[:mid+1]
    
    l, r = 0, len(res) - 1
    while l <= r:
        mid2 = (l+r)//2
        if res[mid2] == target:
            break
        elif res[mid2] < target:
            l = mid2 + 1
        else:
            r = mid2 - 1

    print(f"mid 2: {mid2}")
    if res[mid2] != target:
        return -1
    else:
        if offset != 0: offset = len(nums)  - mid -1
        print(f"offset :{offset}")
        if mid2 >= offset:
            return mid2 - offset
        else: return mid2 + mid + 1
    
print(search([3,1], 3))