# Easy
## 104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Explanation:
The longest path from the root to the farthest leaf node contains 3 nodes.
```
        3
       / \
      9  20
         /  \
        15   7
```

# Key Idea
## Approach 1: DFS (Recursive)
1. Base Case: If `root` is `None`, return `0`
2. Recursive Case:
    - Compute depth of **left subtree**: `dfs(root.left)`
    - Compute depth of **right subtree**: `dfs(root.right)`
    - Return `1 + max(left_depth, right_depth)

## Approach 2: Stack (also DFS)
1. Initialize stack with `(root, depth = 1)`
2. Iterate while the stack is not empty:
    - Pop a node and its depth, update max_depth
    - Push its left and right children into the stack with `depth + 1`
3. Return `max_depth`

## Approach 3: BFS - Queue
1. Initialize a queue with `(root, depth=1)`
2. Iterate while queue not empty:
    - Dequeue a node and its depth
    - Enqueue its **left and right children** with `depth + 1`
3. Return `max_depth`