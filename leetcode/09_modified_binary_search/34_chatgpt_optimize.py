from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    # For easy debug
    indexes = list(range(len(nums)))
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)
    print(f"Indexes: {indexes_str}")
    print(f"Nums:    {nums_str}")
    
    # Helper function to find boundary (first or last occurrence)
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")
            if nums[mid] == target:
                # Store potential boundary index
                bound = mid
                print(f"  🎯 Found {target} at index {mid}. {'Moving left' if is_first else 'Moving right'} to find boundary.")
                if is_first:
                    right = mid - 1  # Search toward the left side for the first occurrence
                else:
                    left = mid  + 1  # Search toward the right side for the last occurrence
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return bound
    return [find_bound(True), find_bound(False)]

print(searchRange([5,7,7,7,7,7,8,8,10], target = 7))
# print(searchRange([2,2], target = 2))