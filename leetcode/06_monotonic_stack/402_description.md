### **Medium**
402. Remove K Digits
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes

#### **Approach**
1. **Use a Monotonic Increasing Stack**:
   - It maintains a **stack** that contains digits in increasing order.
   - If a digit is **smaller than the top of the stack**, it removes the top element to create a smaller number.
   - The stack ensures that the final number remains the smallest possible.

2. **Conditions for removing elements**:
   - We remove elements while `k > 0` and **the top of the stack is greater than the current digit** (ensuring smaller lexicographical order).
   - We also check that removing elements does not reduce the number below the required length (`len(num) - k`).

3. **Handling Leading Zeros**:
   - After constructing the result, leading zeros are removed using `.lstrip('0')`.
   - If the final result is empty (all digits removed), return `"0"`.

---

### **Time and Space Complexity**
- **Time Complexity**: **O(n)** → Each digit is pushed and popped at most once.
- **Space Complexity**: **O(n)** → The stack stores digits in the worst case.

---

### **Example Walkthrough**
#### **Input**: `num = "1432219"`, `k = 3`
#### **Process**:
1. **Start with an empty stack**: `[]`
2. Iterate through `"1432219"`:
   - `'1'` → Stack: `['1']`
   - `'4'` → Stack: `['1', '4']`
   - `'3'` → `'4'` is removed, `k=2`. Stack: `['1', '3']`
   - `'2'` → `'3'` is removed, `k=1`. Stack: `['1', '2']`
   - `'2'` → Stack: `['1', '2', '2']`
   - `'1'` → `'2'` is removed, `k=0`. Stack: `['1', '2', '1']`
   - `'9'` → Stack: `['1', '2', '1', '9']`
3. **Final Stack**: `['1', '2', '1', '9']` → `"1219"`

#### **Output**: `"1219"`
