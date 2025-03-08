# Medium
## 99. Recover Binary Search Tree
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

# Key Idea
## Approach 1 - DFS (Recursive Inorder)
1. Perform inorder traversal `left -> root -> right` to detect misplaced nodes.
2. Identify the two swapped nodes:
    - If a node is smaller than previous node, it indiate swap, store this node into firstNode
    - Do the same to find secondNode
3. Swap the value of firstNode and secondNode

## Approach 2 - DFS - Stack (Iterative Inorder)
1. Use a stack to perform iterative inorder traversal
2. Identify the two swapped nodes using the same method as in Approach 1
