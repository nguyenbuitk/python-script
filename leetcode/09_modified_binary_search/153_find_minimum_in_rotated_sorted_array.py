from typing import List

def findMin(nums: List[int]) -> int:
    # Tạo danh sách index
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")

    left, right = 0, len(nums) - 1
    res = float('inf')
    while left <= right:
        mid = (left + right) // 2
        print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")

        res = min(res, nums[mid])
        
        # Determine which haft is sorted, after that, we can find the minimum value of the sorted haft easily
        if nums[left] <= nums[mid]:
            print("the left haft is sorted")
            res = min(res, nums[left])
            
            # Move pointer to the remaining part to continue find
            left = mid + 1
        else:
            print("the right haft is sorted")
            res = min(res, nums[mid + 1])
            right = mid - 1
    return res

print(findMin([3,1]))