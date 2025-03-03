# Easy
## 94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

# Key Idea
## Approach 1: DFS
1. Base Case: If the current node is `None`, return
2. Recursive Call:
    - Recursively call the function on left child
    - Append the current node's value to the result list
    - Recursively call the function on right child
    

## Approach 2: Stack/Queue
1. Initialize an empty stack and and set `current` to `root`
2. Push **all left node** into the stack until reaching `None`
3. Pop a node, append its value to the result list
4. Move to the right subtree of the popped node
5. Repeats steps 2 - 4 until both the stack is empty and `current` is `None`