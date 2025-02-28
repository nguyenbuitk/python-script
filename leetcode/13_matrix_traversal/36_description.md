# **Medium**
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

# **Key Idea:**
## Approach 1
The goal is to check if a given **9×9 Sudoku board** is valid according to the following rules:
1. **Each row** must contain digits `1-9` **without repetition**.
2. **Each column** must contain digits `1-9` **without repetition**.
3. **Each of the nine 3×3 sub-boxes** must contain digits `1-9` **without repetition**.

## Approach 2
1. Instead of using **three seperate sets** for **rows, columns and 3x3 sub-boxes**, this approach **encodes each constraint as a string** and stores them in a **single HashSet**
    - For each non-empty cell (`board[i][j] != '.'`), create a unique **string identifier** for 
        + **row constraint:** `"(<num>) in row <i>`
        + **column constraint:** `"<j>(<num>)"`
        + **3x3 box constraint:** `"<box_id>(<num>)"`
2. If the same encoded string appears more than once, it means a duplicate exisits
3. Return True

### Visualize approach 2
**Input Sudoku Board**
```
char[][] board = {
    {'5','3','.','.','7','.','.','.','.'},
    {'6','.','.','1','9','5','.','.','.'},
    {'.','9','8','.','.','.','.','6','.'},
    {'8','.','.','.','6','.','.','.','3'},
    {'4','.','.','8','.','3','.','.','1'},
    {'7','.','.','.','2','.','.','.','6'},
    {'.','6','.','.','.','.','2','8','.'},
    {'.','.','.','4','1','9','.','.','5'},
    {'.','.','.','.','8','.','.','7','9'}
};
```
**Tracking the Encoded Strings**
| **Row (`i`)** | **Column (`j`)** | **Digit (`board[i][j]`)** | **Row Constraint** | **Column Constraint** | **Box Constraint** |
|--------------|--------------|------------------|--------------------|------------------|-----------------|
| 0 | 0 | 5 | `(5) in row 0` | `0(5)` | `0(5)0` |
| 0 | 1 | 3 | `(3) in row 0` | `1(3)` | `0(3)0` |
| 1 | 0 | 6 | `(6) in row 1` | `0(6)` | `0(6)0` |
| 1 | 3 | 1 | `(1) in row 1` | `3(1)` | `0(1)1` |
