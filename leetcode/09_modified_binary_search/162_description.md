# Medium
## 162. Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a `0-indexed` integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

# Key Idea
## Approach 1 - Optimize
1. The problem state `nums[-1] = nums[n] = -inf`, ensuring at least one peak exists
2. Binary search insight:
    - if `nums[mid] > nums[mid+1]` -> show that the graph is going down -> exist peak on the left haft
    - if `nums[mid] < nums[mid+1]` -> show that the graph is going up -> exist peak on the right
    