from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    res = float('inf')
    while left <= right:
        mid = (left + right) // 2
        res = min(res, nums[mid])
        print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")
        
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue
        
        if nums[left] <= nums[mid]:
            print("Left haft is sorted")
            res = min(res, nums[left])
            left = mid + 1
            
        else:
            print("Right haft is sorted")
            res = min(res, nums[mid+1])
            right = mid - 1
    return res

findMin([2,2,2,0,1])