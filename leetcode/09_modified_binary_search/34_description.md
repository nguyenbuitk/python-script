# Medium
## 34. Find First and Last Position of Element in Sorted Array
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If target is not found in the array, return `[-1, -1]`.
You must write an algorithm with `O(log n)` runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

# Key Idea
## Approach 1 - Optimize
1. Binary Search for the First Occurrence
    - Perform binary search to locate the first index of the target.
    - If `nums[mid] == target`, store midand continue search toward to the left to find the first occurence
2. Do similar to perform binary search for the last occurence

## Approach 2 - Self
1. Perform bianry search to locate the target
    - If found, set both `min_pos` and `max_pos` to this position
2. Scan left and right to find the first and last occurence

**Notes**: Linear scan `O(n)` after binary search make it less optimal than a pure `O(log n)` solution