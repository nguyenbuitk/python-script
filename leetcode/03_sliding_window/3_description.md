### **Problem Statement**
Given a string `s`, find the **length of the longest substring** without repeating characters.

#### **Examples:**
##### **Example 1:**
**Input:** `s = "abcabcbb"`  
**Output:** `3`  
**Explanation:** The longest substring without repeating characters is **"abc"**, which has a length of `3`.

##### **Example 2:**
**Input:** `s = "bbbbb"`  
**Output:** `1`  
**Explanation:** The longest substring without repeating characters is **"b"**, which has a length of `1`.

##### **Example 3:**
**Input:** `s = "pwwkew"`  
**Output:** `3`  
**Explanation:** The longest substring without repeating characters is **"wke"**, which has a length of `3`.  
Note that **"pwke"** is a subsequence, not a substring.

---

### **Approach: Sliding Window + Hash Set**
Since the problem requires finding the longest substring with unique characters, we can use the **Sliding Window** technique with a **Hash Set** to efficiently track the characters.

#### **Key Idea:**
1. **Use Two Pointers (`left` and `right`)**:
   - The `right` pointer expands the window to include new elements
   - The `left` pointer shrinks when a duplicate appears
2. **Maintain a `current_window`**:
   - Use a **set** to track characters in the current window.
   - If a duplicate character is encountered, move the `left` pointer forward until the window becomes valid again.
3. **Count the valid length**
   - Keep track of the **maximum length** found during this process.
