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
        m = (l + r) // 2
        print(f"\nLeft: {l} ({nums[l]}), Mid: {m} ({nums[m]}), Right: {r} ({nums[r]})")
        if nums[m+1] != nums[m] and nums[m-1] != nums[m]:
            return nums[m]
        
        elif nums[m-1] == nums[m]:
            if (r - m) % 2 == 0:
                print("the left haft contain single value")
                r = m - 2
            else:
                print("the right haft contain single value")
                l = m + 1
        elif nums[m+1] == nums[m]:
            if (r - m) % 2 == 1:
                print("the left haft contain single element")
                r = m - 1
            else:
                print("the right haft contain single element")
                l = m + 2
    return nums[l]

    
    
print(singleNonDuplicate([1,1,2,3,3,4,4]))
print(singleNonDuplicate([1,1,2,2,3,3,4,4,8,8,9]))
print(singleNonDuplicate([8,9,9]))

