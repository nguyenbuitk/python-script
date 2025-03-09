# Medium
## 456. 132 Pattern
Given an array of n integers nums, a 132 pattern is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.
Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

# Key Idea
## Approach 1 - Optimize
1. Initialize a stack to store possible values for `nums[k]` (monotonically decreasing)
2. Traverse `nums` in reverse order
    - If `nums[i] < nums[k]`, return `True`. Because after we have `second ~ nums[k]`, we append `nums[j]` to the stack. So the current pattern is `32`. We just` need to find `1` 
    - While the stack is not empty and the top is smaller than `nums[j]`, update `nums[k]` (`second` variable)
    - Push `nums[j]` onto the stack
3. If no pattern is found, return `False`

## Approach 2 - Self
1. Using two monotonic stacks to store the `smallest left` and `largest of list right smaller`
2. Check for 132 pattern
    - Iterate through two monostacks and check if `stack1[i] < stack2[i]` -> return `True`
    - If not exist, return `False`
