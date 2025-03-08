# Medium 
## 113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.\
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Key Idea
## Approach 1 - DFS Recursive
1. Base case: if `node == None`, return
2. Recursive case: `dfs(node, path = [])`
    - Add `node.val` to `path`
    - If `node` is leaf and `sum(path) == targetSum`, add it to resulut
    - Recursive explore the left and right node

## Approach 2 - DFS Iterative - Stack
1. Initialize a stack with `(node, current_path, current_sum)`
2. Iterate while stack is not emtpy:
    - Pop a node and update path/sum
    - If it's a leaf and sum matches `targetSum`, store the path

## Approach 3 - BFS
1. Initailize a queue with `(node, path, sum)`
2. Iterate while the queue is not empty:
    - Dequeue a node and update the path/sum
    - If it's a leaf and sum matches `targetSum`, store the path
