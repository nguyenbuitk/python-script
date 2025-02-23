### **Medium**
316. Remove Duplicate Letters
Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.


Example 1:
Input: `s = "bcabc"`
Output: `"abc"`

Example 2:
Input: `s = "cbacdcbc"`
Output: `"acdb"`

### Idea 
### Approach Monotonic Stack
## The problem require finding the smallest dictionary with each letter appear exactly once -> using Monotonic Stack to build the resulting 
1. Count the number of occurrences of each character in the string s
2. Iterate through each character in `s` and use the `stack` to store the result
    - If character not in stack:
        + Check if the previous character in the stack is greater and still appears after it, we remove it to keep the smaller dictionary
        + Add the current character to the stack
    - Update the number of occurrences of the character in `s`

### **Ví dụ minh họa**
`a b c d` equal
`1 2 3 4`
#### **Input**: `"bcabc"`
- Đếm số lần xuất hiện: `b:2, c:2, a:1`
- Duyệt từng ký tự:
  1. `'b'`: Stack `[b]`
  2. `'c'`: Stack `[b, c]` và `'c' > 'b'` -> skip
  3. `'a'`: `'a' < 'c'` và `'c'` còn xuất hiện → Loại bỏ `'c'`. `'b' > 'a'` và `'b'` còn xuất hiện → Loại bỏ `'b'`. Stack `[a]`
  4. `'b'`: Stack `[a, b]`
  5. `'c'`: Stack `[a, b, c]`
- **Output**: `"abc"`

#### **Input**: `"cbacdcbc"`
- Đếm số lần xuất hiện: `a:1, b:2, c:4, d:1`
- Duyệt từng ký tự:
  1. `'c'`: Stack `[c]`
  2. `'b'`: `'b' < 'c'` và `'c'` còn xuất hiện -> loại bỏ c -> Stack `[b]` 
  3. `'a'`: `'a' < 'b'` và `'b'` còn xuất hiện → Loại bỏ `'b'`. Stack `[a]`
  4. `'c'`: `'c' > 'a'` stack `[ac]`
  5. `'d'`: `'d' > 'c'` stack `[acd]`
  6. `'c'`: c in stack -> skip
  7. `'b'`: `'b'` < `'d'` nhưng d ko còn xuất hiện -> stack `[acdb]`
  8. `'c'` in stack -> skip

- **Output**: `"acdb"`