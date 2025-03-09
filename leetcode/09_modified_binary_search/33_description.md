# Medium
## 33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index `k (1 <= k < nums.length)` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed)`. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

# Key Idea
## Approach 1: Modified Binary Search
1. **Check if `nums[mid] == target`** → If found, return `mid`.
2. **Determine which half is sorted**:
   - If `nums[left] ≤ nums[mid]` → Left half is sorted.
   - Else, the **right half is sorted**.
3. **Decide where to search next**:
   - If the **left half is sorted**:
      - Check if `target` is within `nums[left] → nums[mid]`.
      - If yes → Move `right` to `mid - 1`.
      - Else → Move `left` to `mid + 1`.
   - Do similar if right haft is sorted

### **Step 3: If Target is Not Found**
- Return `-1`.

## Approach 2: Self
1. Use binary search to locate the pivot.
2. Transform the array into a sorted array.
   - If no rotation is found, the array remains unchanged
   - If a pivot is found, construct a new array starting from the pivot to create sorted array
3. Search for the target using Binary Search
