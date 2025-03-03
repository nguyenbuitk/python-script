# Easy
## 463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Key Idea
## Approach 1: Count-Based (Optimal)
1. Iterate through **each cell** in the grid:
    - If the cell is **land** (`1`), assume it adds `+4` to the perimeter.
    - Check the **top** and **left** neighbors:
        - If the top neighbor is also land, subtract `-2` (they share an edge)
        - If the left neighbor is also land, subtract `-2`
2. Return `perimeter`

### Time & Space Complexity
    - Time Complexity: `O(m * n)`
    - Space: O(1) -> no extra space used
### Example Walkthrough
### Input
```python
grid = [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
]
```

### **Step-by-Step Execution**
| Cell | Initial `+4` | Shared Edges (Subtract `-2`) | Cumulative Perimeter |
|------|-------------|-----------------------------|----------------------|
| `(0,1)` | `+4` | No neighbors | `4` |
| `(1,0)` | `+4` | No neighbors | `8` |
| `(1,1)` | `+4` | `(0,1)` (top) `-2`, `(1,0)` (left) `-2` | `8` |
| `(1,2)` | `+4` | `(1,1)` (left) `-2` | `10` |
| `(2,1)` | `+4` | `(1,1)` (top) `-2` | `12` |
| `(3,0)` | `+4` | No neighbors | `16` |
| `(3,1)` | `+4` | `(3,0)` (left) `-2` | `16` |


## Approach 2: DFS
1. Start from any land cell `1`
2. Base Cases:
    - If out of bounds or water, count it as perimeter (`+1`)
        ```
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 1
        ```
    - If already visted, return 0
### Time & Space Complexity
    - Time Complexity: `O(m * n)`
    - Space: O(1) -> no extra space used