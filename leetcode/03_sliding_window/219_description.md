# **Easy**
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

# **Key Idea:**
1. **Use Two Pointers (`left` and `right`)**:
   - The `right` pointer expand the windows to include new element
   - The `left` pointer shrinks when a window size exceed `k`
2. **Maintain a `current_window`**:
   - Use a **hash** to track characters in the current window
   - If new character appear in **hash**, return True, else add new character to **hash** and shrink window
