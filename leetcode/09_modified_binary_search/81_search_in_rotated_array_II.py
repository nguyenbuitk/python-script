from typing import List
import time
def search(nums: List[int], target: int) -> bool:
    # Print with list and index
    indexes = list(range(len(nums)))
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)
    print(f"Indexes: {indexes_str}")
    print(f"Nums:    {nums_str}")
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")

        if nums[mid] == target:
            return True
        print(f"nums[left] = {nums[left]}")
        print(f"nums[mid] = {nums[mid]}")
        print(f"min(nums[left:mid+1])= {min(nums[left:mid+1])}")
        print(f"max(nums[left:mid+1])= {max(nums[left:mid+1])}")
        print(f"min(nums[mid:right+1]) = {min(nums[mid:right+1])}")
        print(f"max(nums[mid:right+1]) = {max(nums[mid:right+1])}")
        if nums[left] < nums[mid] or (nums[left] == nums[mid] and min(nums[left:mid+1]) == nums[mid] and max(nums[left:mid+1]) == nums[mid]):
            print("The left haft is sorted")
            if nums[left] <= target < nums[mid]:
                print(f"Target {target} is in sorted part. Moving right pointer to {mid - 1}")
                right = mid - 1
                
            else: 
                left = mid + 1
                print(f"Target {target} is not in sorted part. Moving left pointer to {mid + 1}")
        elif nums[left] > nums[mid] or (nums[left] == nums[mid] and min(nums[mid:right+1]) == nums[mid] and max(nums[mid:right+1]) == nums[mid]):
            print("The right haft is sorted")
            # Check if the target is in the sorted haft
            if nums[mid] < target <= nums[right]:
                print(f"Target {target} is in sorted part. Moving left pointer to {mid+1}")
                left = mid + 1
            else:
                print(f"Target {target} is not in sorted part. Moving right pointer to {mid-1}")
                right = mid - 1

        time.sleep(0.5)
    return False
# print(search([4,5,6,7,8,-2,-1,0,1,2,3,3,3], 0))
print(search([1,0,1,1,1],0))
