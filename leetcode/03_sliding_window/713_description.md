# **Medium**
713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

# **Approach: Sliding Window (Two Pointers)**
We can efficiently solve this problem using a **sliding window** approach.

1. **Use Two Pointers (`left` and `right`)**:
   - The `right` pointer expands the window to include new elements.
   - The `left` pointer contracts the window when the product becomes **greater than or equal to `k`**.

2. **Maintain a `current_window` product**:
   - Multiply the new element to `current_window` as `right` expands.
   - If `current_window` **>= k**, divide by `nums[left]` and move `left` forward.

3. **Count the Valid Subarrays**:
   - Every time `right` expands, **all subarrays ending at `right` and starting from `left` to `right` are valid**.
   - The count of valid subarrays **is `(right - left + 1)`**.
