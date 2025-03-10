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
## Approach 1: Modified Binary Search - Chatgpt
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
   - If a pivot is found, construct a new array starting from the pivot to create sorted array by store an offset.
3. Search for the target using Binary Search

## Approach 3: Community 1
**Notes** Similar to approach 2 but with more efficient algorithm
1. Use binary search to locate the pivot
    - `while(l < r): if nums[mid] > nums[left], move right, else move left`
2. Modified Binary Search
    - Search in rotated array by adjusting `mid` using `(mid+pivot)%n` to find `realmid`
    - Compare `nums[realmid]` with target and move left, right arcodingly
        - `realmid` is moved to new position after rotate rot times
        - That is reason why `realmid = (mid + rot)%n`

## Approach 4: Community 2
1. If `nums[mid]` and `target` are on the smae side of `nums[0]`, use `nums[mid]` directly
2. Otherwise, map `nums[mid]` to inf or -inf to force binary search in the right direction

**Example**
Let's say nums looks like this: `[12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
`[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]`

If target is let's say 7, then we adjust nums to this:
`[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

And then we can simply do ordinary binary search. Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at
