# Medium
658. Find K Closest Elements
Given a sorted integer array arr, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.
An integer `a` is closer to `x` than an integer `b` if:
`|a - x| < |b - x|`, or
`|a - x| == |b - x|` and `a < b`
 
Example 1:
Input: arr = [1,2, ,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]

# **Approach: Sliding Window**
1. **Find the Position of `x` (or the closest index)**
   - Use **Binary Search** to locate the first element `arr[i]` where `arr[i]>=x`
2. **Expand Two Pointers (`left` and `right`)**
   - Start with:
     - `left = i - 1` (just before `x`)
     - `right = i` (just after `x`)
   - Expand **k times**, always choosing the closest element first.

3. **Sort and Return the `k` Elements**
   - Since elements are picked from **both sides**, sort before returning.
