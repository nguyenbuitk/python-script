# Medium
## 74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

# Key Idea
## Approach 1
1. Since each row is sorted, we can use binary search to find `target` eficiently
2. If the last element of a row is smaller than `target`, skip the row

## Approach 2 (community)
1. Since each row is sorted, and the first number of each row is greater than the last number of the previous row, we can treat the 2D matrix as a 1D sorted array
    - Convert **(row, col)** -> **index** using:
        + `index = row*m + col`
    - convert **index** -> **(row, col)** using:
        + `row = index/m`
        + `col = index%m`
2. We perform **Binary Search** directly on this flattened version of the matrix
