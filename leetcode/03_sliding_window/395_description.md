395. Longest Substring with At Least K Repeating Characters
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
if no such substring exists, return 0.
Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


## **Binary Search + Sliding Window**
### **Steps**
1. **Use Binary Search to Find the Best Starting Index**
   - Instead of using two pointers, perform **binary search** on `arr` to find the **left boundary** of the best `k` elements.

2. **Sliding Window**
   - After binary search, adjust the window of `k` elements to ensure it is the closest to `x`.

3. **Return the Window**
   - Since `arr` is already sorted, no additional sorting is needed.

