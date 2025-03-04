# Easy
## 404. Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Key Idea
## Approach 1: DFS
1. Base Case: If `root` is `None`, return 0
2. Recursive Case:
    - Create `dfs(node, isLeftNode: bool)`
    - If `root.left` is a leaf, add it value
    - Recur on `root.left` with `True` and `root.right` with `False` to find more left leaves
**Time and Space complexity**
- Time complexity: `O(n)`, since each node is visited once.
- Space complexity: `O(h)`, where `h` is height of tree

## Approach 2: Stack (also DFS)
1. Initialize a stack with `(root, False)` where `False` mean "not a left child"
2. Iterate while stack is not empty:
    - Pop a node and check if it's a left leaf
    - Push right and left children to the stack
**Time and Space complexity**: Similar DFS

## Approach 3: BFS
1. Initialize  a queue with a `(root, False)`
2. Iterate while the queue is not empty:
    - Dequeue a node, check if it's a left leaf
    - Enqueue left and right children if they exist.
**Time and Space complexity**
- Time complexity: `O(n)`, since each node is visited once.
- Space complexity: `O(w)`, where `w` is maximum width of tree