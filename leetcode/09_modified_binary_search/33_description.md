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
## **2️⃣ Algorithm (Modified Binary Search)**
### **Step 1: Initialize Search Bounds**
- Set `left = 0`, `right = len(nums) - 1`.

### **Step 2: Perform Binary Search**
- While `left <= right`:
  1. Compute **midpoint**:  
     ```python
     mid = (left + right) // 2
     ```
  2. **Check if `nums[mid] == target`** → If found, return `mid`.
  3. **Determine which half is sorted**:
     - If `nums[left] ≤ nums[mid]` → Left half is sorted.
     - Else, the **right half is sorted**.
  4. **Decide where to search next**:
     - If the **left half is sorted**:
       - Check if `target` is within `nums[left] → nums[mid]`.
       - If yes → Move `right` to `mid - 1`.
       - Else → Move `left` to `mid + 1`.
     - If the **right half is sorted**:
       - Check if `target` is within `nums[mid] → nums[right]`.
       - If yes → Move `left` to `mid + 1`.
       - Else → Move `right` to `mid - 1`.

### **Step 3: If Target is Not Found**
- Return `-1`.
