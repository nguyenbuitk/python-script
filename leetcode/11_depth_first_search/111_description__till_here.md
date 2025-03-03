# Easy
## 111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2
Explanation:
The shortest path from the root to a leaf node contains 2 nodes.

        3
       / \
      9  20
         /  \
        15   7

# Key Idea
## Approach 1: DFS
**Note**: Special case: if one subtree is `None`, we must take the non-null subtree's depth instead of taking `min(left, right)`
1. Base Case: If `root` is `None`, return 0
2. Recursive Case:
    - If one child is missing, return `1 + depth of the non-null subtree`
    - If both children exist, return `1 + min(left_depth, right_depth)`

## Approach 2: Stack
1. Khởi tạo stack với `(root, depth = 1)`
2. Duyệt cây bằng DFS (Stack):
    - Pop `(node, depth)` từ stack.
    - Nếu `node` là `leaf`, cập nhật min_depth.
    - Nếu có con trái, `push (node.left, depth + 1)`.
    - Nếu có con phải, `push (node.right, depth + 1)`.
    - Trả về min_depth nhỏ nhất sau khi duyệt xong.

## Approach 3: BFS
The first leaf node encoutered gives the minimum depth.
1. Initialize a queue with `(root, depth = 1)`
2. Loop until queue is empty:
    - Dequeue `(node, depth)` (pop queue)
    - If `node` is a lefaf, return `depth`
    - Enqueue **left and right children** with `depth + 1`