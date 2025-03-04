# Medium
## 98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
```
      5
     / \
    1   7
       / \
      3   6
```
Input: root = [5,1,4,null,null,3,6]
Output: false 

# Key Idea
## Approach 1: DFS
1. Base Case: if a node is `None`, return `True`
2. Traverse the tree recursively
    - Create `dfs(node)`
    - If `node.left` not `None` and it has greater equal value than node.val, return `False`
    - Recursively call `return dfs(node.left) and dfs(node.right)`