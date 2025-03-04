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
## Visualize noted on draw.io
## Approach 1: DFS
1. Base Case: if a node is `None`, return `True`
2. Traverse the tree recursively
    - Create `dfs(node, minVal, maxVal)`. Keeping track of valid value range
    - Left subtree -> update `maxVal = node.val`
    - Right subtree -> update `minVal = node.val`
    - Recursively call `return dfs(node.left, minVal, node.Val) and dfs(node.right, node.val, maxVal)`

## Approach 2: DFS - Inorder traversal
1. A valid BST has an inorder traversal that is stricly increaasing
2. Use inorder traversal `(Left -> Root -> Right)`
      - Keep track of the last visited value (`preVal`)
      - If the current val is <= `preVal`, return `False`, else continue

## Approach 3: DFS - Stack
Smilar to approach 2, but use a stack to avoid recursion\
1. Initialize a stack and set `preVal = float('-inf')`
2. Process in order and track the `preVal` value, similar to approach 2

## Approach 4: BFS
Maintain valid value range `(minVal, maxVal)` for each node
1. Initailize a queue with `(node, minVal, maxVal)`
2. Iterate over queue
    - If `node.val` out of range, return `False`
    - Push `(node.left, minVal, node.val)` and `(node.right, node.val, maxVal)` to queue
