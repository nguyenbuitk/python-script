from typing import List
import time
def findPeakElement(nums: List[int]) -> int:
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
    
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        print(f"Left: {left} ({nums[left]}), Mid: {mid} ({nums[mid]}), Right: {right} ({nums[right]})")
        if nums[mid] > nums[mid+1]:
            print("graph is going down, exist peak in the left haft")
            # mid still can be the peak
            right = mid
        else:
            print("graph is going up, exisit peak in the right haft")
            # mid can't be the peak, skip mid
            left = mid + 1
        time.sleep(0.5)
    return left

findPeakElement([1,2,1,3,5,6,4])