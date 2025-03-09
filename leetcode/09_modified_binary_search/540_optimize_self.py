from typing import List

def singleNonDuplicate(nums: List[int]) -> int:
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
    
    l, r = 0, len(nums) - 1
    # number of element = 2n + 1
    # each time remove 2*x -> it have 3 elements left near the end
    while l < r:
        m = (l+r) // 2
        if m%2 != 0:
            m -= 1
        if nums[m] == nums[m+1]:
            print("The right haft contain single element")
            l = m + 2
        else:
            print("The left haft contain single element")
            r = m
            
    return nums[l]

print(singleNonDuplicate([1,1,2,3,3,4,4]))
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8,9,9]))
print(singleNonDuplicate([8,9,9]))

