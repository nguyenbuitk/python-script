# **Easy**
594. Longest Harmonious Subsequence
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2

# **Key Idea**
1. **Use a HashMap (`frequency_map`)**:
    - Store the frequency of number in `nums`
    - This allow us to quickly check if a number `x + 1` exists when processing `x`
2. **Iterate through Unique Keys**:
    - For each unique number `x` in `frequency_map`, check if `x + 1` exists.
    - If `x+1` exists, compute the length of the harmonious subsequence as `frequency_map[x] + frequency_map[x+1]`
