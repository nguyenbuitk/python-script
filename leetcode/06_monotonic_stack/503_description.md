### **Medium**
503. Next Greater Element II
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 
Example 1:
Input: nums = `[1,2,1]`
Output: `[2,-1,2]`
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = `[1,2,3,4,3]`
Output: `[2,3,4,-1,4]`

### **Monotonic Stack**
Approach 1
1. Iterate twice over nums (simulate cirular by extending array length to 2*len)
    - For example: with array `[1, 4, 2, 6]`, we will iterate through `[1, 4, 2, 6, 1, 4, 2, 6]`
2. Use a decreasing stack, if `nums[i]` equal or greater than top of the stack, pop element from stack

Approach 2 (self)
1. Instead of iterating over 2*N (as in the classical approach), the loop manually initializes the stack using the rightmost elements.
