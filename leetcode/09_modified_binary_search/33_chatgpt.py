from typing import List

def search(nums: List[int], target: int) -> int:
    # Tạo danh sách index
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]: 
            print("Left haft is sorted")
            if nums[left] <= target < nums[mid]:
                print(f"Target {target} is in left haft. Moving right pointer to {mid - 1}")
                right = mid - 1
            else:
                print(f"Target {target} is not in left haft. Moving left pointer to {mid + 1}")
                left = mid + 1
        else:
            print("Right haft is sorted")
            if nums[mid] < target <= nums[right]:
                print(f"Target {target} is in right haft. Moving left pointer to {mid + 1}")
                left = mid + 1
            else:
                print(f"Target {target} is not in right. Moving right pointer to {mid - 1}")
                right = mid - 1
    return -1

# Example Usage
print("Test 1 #############")
nums = [5,1,2,3,4]
target = 1
print(search(nums, target))  # Expected Output: 4

