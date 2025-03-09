from typing import List
import time

def searchRange(nums: List[int], target: int) -> List[int]:
    indexes = list(range(len(nums)))
    
    # Print with list and index
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)
    
    print(f"Indexes: {indexes_str}")
    print(f"Nums:    {nums_str}")
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")
        if nums[mid] == target:
            min_pos = mid
            max_pos = mid
            print(f"mid: {mid}")
            
            # Linear scan to find the first position
            for i in range(mid - 1, -1, -1):
                if nums[i] == target:
                    min_pos = min(i, min_pos)
                    
            # Linear scan to find the last position
            for i in range(mid+1, len(nums)):
                if nums[i] == target:
                    max_pos = max(i, max_pos)
                
            return [min_pos, max_pos]
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]

# print(searchRange([5,7,7,8,8,10], target = 6))
print(searchRange([2,2], target = 2))