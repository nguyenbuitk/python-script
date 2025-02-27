### Medium
## 395. Longest Substring with At Least K Repeating Characters
Given a string `s` and an integer `k`, return the length of the longest substring where each character appears at least `k` times. If none exists, return `0`.

### Example 1:
**Input:** `s = "aaabb"`, `k = 3`  
**Output:** `3` (`"aaa"`)

### Example 2:
**Input:** `s = "ababbc"`, `k = 2`  
**Output:** `5` (`"ababb"`)

### **Approach 1: Divide and Conquer (Recursive Splitting)**
#### **Intuition**
- If a character occurs **less than `k` times**, it **cannot be part of any valid substring**.
- We can use this character as a **split point** to divide the string into **smaller substrings** and recursively check them.

#### **Steps**
1. **Count the frequency** of each character in the string.
2. **Find the first character** that occurs **less than `k` times**.
3. **Use it as a split point** to divide `s` into **smaller substrings**.
4. **Recursively apply the same process** on each substring.
5. **Return the maximum valid substring length**.

#### **Complexity Analysis**
- **Time Complexity:** `O(N^2)` in the worst case (multiple recursive splits).
- **Space Complexity:** `O(N)` (recursion stack).

---

### **Approach 2: Sliding Window with Unique Character Count**
#### **Intuition**
- If we **fix the number of unique characters** in a window and check if all of them appear at least `k` times, we can find the **longest valid substring**.
- We iterate over different values of unique character count (`1 → 26` for lowercase letters).

#### **Steps**
1. **Iterate over unique character counts** (from `1 → 26` since there are at most `26` lowercase letters).
2. **Use Sliding Window** to expand `right` pointer while keeping track of:
   - **Character frequency**
   - **Number of unique characters**
   - **Number of characters that appear at least `k` times**.
3. **When conditions are met**, update the result.
4. **Move `left` pointer** to ensure that the number of unique characters doesn't exceed the current limit.
