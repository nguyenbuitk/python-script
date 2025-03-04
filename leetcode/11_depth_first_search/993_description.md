# Easy
## 993. Cousins in Binary Tree
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```
     1
    / \ 
   2   3
 /
4
```

# Key Idea
## Approach 1: DFS
1. Base Case: If a node is `None`, return
2. Traverse the tree recursively while keep track of `Depth of each node` and `Parent of each node`
3. Recursive Case:
    - If `node.val == x or node.val == y`, stores it `depth` and `parent`
4. After DFS traversal:
    - Check x_depth, y_depth and x_parent, y_parent
**Time and Space Complexity**
- Time: `O(n)`
- Space: `O(h)`

## Approach 2: Stack - DFS
1. Initialize a stack `(node, parent, depth)`
2. Iterate while stack is not empty
    - Keep track of each node's depth and parent.
    - If both x and y are found: Check if they have the same depth but different parents.

## Approach 3: BFS - Queue
1. Initialize a queue with `(node, parent)`
2. Perform BFS:
    - Iterate all queue by using `len(queue)` to get all current level of tree
    - For each node: if `node.val == x or node.val == y`, store its parent
    - If both are found, check if they have different path
**Time and Space Complexity**
- Time: `O(n)`
- Space: `O(w)`