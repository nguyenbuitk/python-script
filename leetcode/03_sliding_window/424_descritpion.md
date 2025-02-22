### **Problem Statement**
Given a string `s` and an integer `k`, you can replace **at most** `k` characters in `s` with any other uppercase English character.  
Return the **length of the longest substring** that contains the **same letter** after performing the allowed operations.

---

### **Examples**
#### **Example 1**
**Input:**  
`s = "ABAB", k = 2`  
**Output:**  
`4`  
**Explanation:**  
Replace the two `'A'`s with `'B'`s or vice versa, forming `"BBBB"` or `"AAAA"`, both of which have length `4`.

---

#### **Example 2**
**Input:**  
`s = "AABABBA", k = 1`  
**Output:**  
`4`  
**Explanation:**  
Replace the middle `'A'` with `'B'` to form `"AABBBBA"`.  
The longest substring is `"BBBB"`, which has length `4`.  
Other possible answers also exist.



### **Approach: Sliding Window (Two Pointers)**

#### **1. Use Two Pointers (`left` and `right`)**
- The `right` pointer expands the window to include new elements.
- The `left` pointer shrink the window when more than `k` replacements are needed.

#### **2. Adjust the window**

- If more than `k` replacements are needed (`(right - left + 1) - max_freq > k`), shrink the window by moving `left` to the right.
- Reduce the frequency count of the leftmost character while shrinking the window.

#### **3. Track the Maximum Substring Length**
- The valid substring length is `(right - left + 1)`, and we update the `max_length` accordingly.
