### **Medium**
567. Permutation in String
Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or false otherwise.

In other words, return true if one of `s1's` permutations is the substring of `s2`. 

Example 1:
Input: `s1 = "ab", s2 = "eidbaooo"`
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: `s1 = "ab", s2 = "eidboaoo"`
Output: false
 

### **Approach: Sliding Window**
1. Calculate the frequency of character in `s1`
2. Use another frequency counter for a sliding windows of length `len(s1)` in `s2`
2. Use two pointers (`left` and `right`):
   - The `right` pointer expand the windows to include new elements
   - The `left` pointer shrink the windows
3. If the windows contain all chacter of s1, return True
4. If no match is found after checking all windows -> return False
