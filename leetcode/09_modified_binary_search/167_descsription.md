# Medium
## 167. Two Sum II - Input Array Is Sorted
Given a `1-indexed` array of integers numbers that is already sorted in `non-decreasing order`, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.
Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

# Key Idea
## Approach 1: two pointer
1. Since the array is sorted, we can use the `two-pointer` technique.
2. Instead of using binary search (O(n log n)) or a hash map (O(n)), we maintain two pointers:
    - If `numbers[left] + numbers[right] == target`, return the indices.
    - If the sum is too small, increase left (move right).
    - If the sum is too large, decrease right (move left).
**Complexity**: O(n) time and O(1) space

## Approach 2: binary search
1. Get one element and search the rest of array
**Complexity**: O(nlogn) time and O(1) space