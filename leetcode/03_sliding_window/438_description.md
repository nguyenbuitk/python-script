# **Medium**
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
*Trả về array chứa tất cả các index bắt đầu của các hoán vị p chứa trong s*
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

# **Key Idea**
**Approach: Sliding Window**
1. Calculate the frequency of character in `p`
2. Use another frequency counter for a sliding windows of length `len(p)` in `s`
3. Use two pointers (`left` and `right`):
   - The `right` pointer expand the windows to include new elements
   - If the windows contain all chacter of s, add index
   - move `left` pointer to 1 index `left += 1` to maintain the length of window
