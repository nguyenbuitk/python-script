from typing import List

def search(nums: List[int], target: int) -> bool:
    # Example: [6,7,8,9,10,11,0,1,2,3]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        
        # handle duplicated case
        ## for ex:   5 5 5 5 5 5(mid) 5 1 2 3 4 5
        ##           5 6 7 8 9 5(mid) 5 5 5 5 5 5
        if nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1
            continue
        
        if nums[left] <= nums[mid]:
            # left haft is sorted
            if nums[left] <= target < nums[mid]:
                # target in sorted part, move right pointer to mid -1
                right = mid - 1
            else:
                # target not in sorted part, move left pointer to mid + 1
                left = mid + 1
        else:
            # nums[left] > nums[mid] -> right haft is sorted
            if nums[mid] < target <= nums[right]:
                # target in sorted part
                left = mid + 1
            else:
                right = mid -1 
    return False