# Medium
## 540. Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

# Key Idea
1. Use binary search to efficiently locate the single element
2. If `mid` is even, its pair should be at `mid+1`
3. If `mid` is odd, its pair should be at `mid-1`
4. If the pair matches, then the single elment is in the right haft, otherwise the single element is in the left haft