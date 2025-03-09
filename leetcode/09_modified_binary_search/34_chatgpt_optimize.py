from typing import List
import time

def searchRange(nums: List[int], target: int) -> List[int]:
    # Print with list and index
    indexes = list(range(len(nums)))
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)
    print(f"Indexes: {indexes_str}")
    print(f"Nums:    {nums_str}")
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")
            if nums[mid] == target:
                bound = mid
                print(f"  🎯 Found {target} at index {mid}. {'Moving left' if is_first else 'Moving right'} to find boundary.")
                if is_first:
                    right = mid - 1
                else:
                    left = mid  + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return bound
    return [find_bound(True), find_bound(False)]
print("############ Test 1 ############")
print(searchRange([5,7,7,7,7,7,8,8,10], target = 7))
# print(searchRange([2,2], target = 2))