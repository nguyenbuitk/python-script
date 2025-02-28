# **Medium**
## 48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. 

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

# **Key Idea**
## Approach 1
1. Convert rows into columns by swapping `matrix[i][j]` with `matrix[j][i]`
2. Reverse each row. After trasnposition, reverse each row to get the final rotated matrix

## Approach 2
1. To rotate 90 c, we need convert each element `(i, j)` moves to `(j, n - i -1)`
    - For example: `(0, 1)` -> `(1, 3-1-1)` = `(1, 2)`
    - `(0, 2)` -> `(2, 3 -1 -0)` = `(2, 2)`

2. To convert `(i, j)` moves to `(j, n - i -1)`. We using two steps
    - Convert `(i, j)` to `(n -i -1, j)` (by reverse the matrix vertically)
    - Swap `(n - i -1, j)` to `(j, n -i -1)`

