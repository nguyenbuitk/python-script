### **Medium**

739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

### Idea **Monotonic Stack**
1. Iterate backwards throught the `temparatures` array
2. Use a stack to store indices of temperatures in decreasing order
3. For each temperature at index `i`:
    - Remove elements from the stack **while the top of the stack is less or equal to `temperatures[i]`**
    - If stack is not empty, the top element represents **the next greater temperatures**, so compute res[i] = stack[-1] - i (days to wait)
    - Push (temperature, index onto the stack)