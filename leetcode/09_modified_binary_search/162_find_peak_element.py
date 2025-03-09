from typing import List

def findPeakElement(nums: List[int]) -> int:
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        break

findPeakElement([1,2,1,3,5,6,4])