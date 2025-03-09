# Medium
## 81. Search in Rotated Sorted Array II

There is an integer array `nums` sorted in non-decreasing order (not necessarily with distinct values).\
Before being passed to your function, `nums` is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index 5 and become `[4,5,6,6,7,0,1,2,4,4]`.\
Given the array `nums` after the rotation and an integer `target`, return true if target is in nums, or false if it is not in nums.\
You must decrease the overall operation steps as much as possible.\

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

# Key Idea
## Approach 1 - Self
Notes: Unlike problem 33, this version allow duplicate values.
If `nums[left] == nums[mid] == nums[right]`, we can't determine which haft is sorted.
1. In this approach, we handling duplicate by checking the `max` and `min` of the haft to determine which haft is sorted.
2. After determine the sorted haft, we continue do similar to problem 33 `search in rotated array`

## Approach 2 - Optimize
1. After perform binary search, we need to handle duplicate case:
    - If `nums[left] == nums[mid] == nums[right]`, move `left+=1, right+=1`
2. After handle duplicate, we do similar to **problem 33**
    - Identify which haft is sorted
    - Determine whether target is in sorted haft or not and moving pointer appropriately