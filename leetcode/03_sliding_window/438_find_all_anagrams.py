"""
### **Medium**
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
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
"""

import collections
def findAnagrams(s, p):
    res = []
    len_s, len_p = len(s), len(p)

    # edge case: if p is longer than s, no anagrams are posible
    if len_s < len_p: return res
    
    # Step 1: create frequency
    counter_p = collections.Counter(p)
    counter_s = collections.Counter(s[:len_p])
    
    if counter_s == counter_p:
        res.append(0)
    
    # Step 2: slide the window across s
    for i in range(len_p, len_s):
        # Add the new character at the right end of the window
        counter_s[s[i]] += 1
        
        # Remove the character that moves out of the left end
        counter_s[s[i-len_p]] -= 1
        
        # If count of character equal 0, remove it to make dictionary clean
        if counter_s[s[i-len_p]] == 0:
            del counter_s[s[i-len_p]]
        
        # Add starting index if current window match p's frequency
        if counter_p == counter_s:
            res.append(i - len_p + 1)
    
    return res        
    
print(findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa"))
