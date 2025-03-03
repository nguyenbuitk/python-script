# Medium
## 79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

# Key Idea
## Approach 1. DFS - Stack-based
1. Iterate over every cell in the matrix
2. For each matching starting cell (`board[i][j] == word[0]`)
    - Initialize a `stack` to simulate DFS
    - Use a `visited` set to keep track of explored path
3. Iteratively explore teh boad
    - Push valid moves to the stack
    - If `word[k]` is found in sequence, continue
    - If the path is valid, `backtrack` (pop the stack, remove from `visited`, decrement `k`)

### **Example Input:**
We will step through the **stack-based DFS approach** using the test case:

```plaintext
Board:
C  A  A
A  A  A
B  C  D
```
**Word:** `"AAB"`

🔹 **We start from (1,1) → 'A'**  
## **🔹 Summary of Moves**
A stand for position of A\
mR, mL, mU, mD stand for moveRight, moveUP, ...
| Step | Position `(row, col)` | Stack State | Visited Nodes | Next Move |
|------|----------------|------------|--------------|------------|
| 1️⃣ | `(1,1 - A)` | `[((A), [])]` | `{}` | Move to `(A-right)` |
| 2️⃣ | `(1,2 - A-right)` | `[((A), [mR]), ((A-right), [])]` | `{(A), (A-right)}` | No valid moves → Backtrack: stack.pop() visited.remove((m,n)) (m,n is A-right)  |
| 3️⃣ | `(1,1 - A)` | `[((A), [mR])]` | `{(A)}` | Move to `(A-left)` |
| 4️⃣ | `(0,1 - A-left)` | `[((A), [mR, mD]), ((A-left), [])]` | `{(A), (A-left)}` | Move to `(B)` |
| 5️⃣ | `(0,2 - B)` | `[((A), [mR, mD]), ((A-left), [mD]), ((B), [])]` | `{A, A-left, B}` | word = "AAB" -> return True |

## Approach 2. Optimized DFS with backtracking
1. DFS with backtracking:
    - Start searching from each cell `(i, j)`
    - If the character at `board[i][j]` matches the first letter of `word`, initiate a DFS to explore all possible paths
2. Perform DFS with Backtracking:
    - If the entire `word` is found (`k == len(word) - 1`), return True
    - Mark the vistied cells to avoid resuing them in the same search path
    - Move in 4 possible directions and ocntinue searching for `word[k+1]`
    - If no valid path is found, backtrack
3. If no valid path found for any starting cell, return `False`

# Example
## Using DFS
### **Flow to Solve Test Case:**
**Board:**  
```
A B C E
S F C S
A D E E
```
**Word:** `"ABCB"`  
**Approach:** **DFS (Depth-First Search) with Backtracking**  
### **Step-by-Step Execution**
1. **Start DFS from each occurrence of the first letter 'A' in the board.**
   - Possible **starting points:** `(0,0)` and `(2,0)`.
   - **First match found at (0,0)**, so we begin DFS from `(0,0)`.

---

### **Step 1: Start DFS from (0,0)**
- Current letter: `'A'`
- Match found (`board[0][0] == 'A'`).
- Mark **(0,0) as visited**.
- Move right `dr, dc = 0, 1` to the **next character `'B'`**.

#### **Exploring Directions from (0,0):**
✅ Move **right** `(0,1) → 'B'` → Matches! Continue.  

---
### **Step 2: Move to (0,1)**
- Current letter: `'B'`
- Match found (`board[0][1] == 'B'`).
- Mark **(0,1) as visited**.
- Move right `dr, dc = 0, 1` the **next character `'C'`**.

#### **Exploring Directions from (0,1):**
✅ Move **right** `(0,2) → 'C'` → Matches! Continue.

---

### **Step 3: Move to (0,2)**
- Current letter: `'C'`
- Match found (`board[0][2] == 'C'`).
- Mark **(0,2) as visited**.
- Move to the **next character `'B'`**.

#### **Exploring Directions from (0,2):**
- Move **right** `(0,3) → 'E'` ❌ No match.
- Move **down** `(1,2) → 'C'` ❌ No match.
- Move **left** `(0,1) → 'B'` ❌ Already visited.
- Move **up** ❌ Out of bounds.

⛔ **No valid moves left!** → **Backtrack from (0,2).**

---

### **Step 4: Backtrack to (0,1)**
- Unmark **(0,2) from visited**.
- Try other directions from **move right** `(dr, dc) = (0,1)` (move down, move left)

#### **Exploring Other Directions from (0,1):**
- Move **down** `(1,1) → 'F'` ❌ No match.
- Move **left** `(0,0) → 'A'` ❌ Already visited.

⛔ **No valid moves left!** → **Backtrack from (0,1).**

---

### **Step 5: Backtrack to (0,0)**
- Unmark **(0,1) from visited**.
- Try other directions from **move right** `(dr, dc) = (0,1)`. (move down)

#### **Exploring Other Directions from (0,0):**
- Move **down** `(1,0) → 'S'` ❌ No match.

⛔ **No valid moves left!** → **Backtrack from (0,0).**  
- **Starting from (0,0) does NOT form the word "ABCB".**

---

### **Step 6: Try Other 'A' at (2,0)**
- Current letter: `'A'`
- **Match found (`board[2][0] == 'A'`)**.
- **DFS again**, but fails at `'B'` like the previous attempt.

⛔ **Backtrack and mark test case as False.**

---

### **Final Result**
Since no path successfully forms `"ABCB"`, we return **`False`**.

---

### **Summary of Steps**
| Step | Position | Letter | Action | Next Move |
|------|----------|--------|--------|-----------|
| 1 | (0,0) | A | Start DFS | Move right (0,1) |
| 2 | (0,1) | B | Continue DFS | Move right (0,2) |
| 3 | (0,2) | C | Continue DFS | No valid move (Backtrack) |
| 4 | (0,1) | B | Backtrack | No valid move (Backtrack) |
| 5 | (0,0) | A | Backtrack | No valid move (Try next 'A') |
| 6 | (2,0) | A | Start DFS | Fails at 'B' |
| - | - | - | No valid path found | **Return False** |

---

### **Final Answer:**
🚫 **`False` (Word "ABCB" does not exist in the board).**