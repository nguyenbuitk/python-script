from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    def binarySearch(nums: List[int], target):
        print(f"target: {target}")
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return None
    for i in range(len(numbers)):
        print(f"number[{i}]: {numbers[i]}")
        index2 = i + 1
        index1 = binarySearch(numbers[:i], target - numbers[i])
        if index1 != None:
            return [index1 + 1, index2]
    return False
print(twoSum([2,7,11,15], 22))
