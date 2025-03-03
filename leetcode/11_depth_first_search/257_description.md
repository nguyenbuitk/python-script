# Easy
## 257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

# Key Idea
## Approach 1 - DFS
1. Base Case: If node is `None`, return
2. Recursive Case:
    - Append the current node value to path
    - If the node is a leaf, add the path to result
    - If the node has left/right chilred, recurse on the mwith the updated path

**Time and Space Complexity**
1. Time: `O(n)`, where n is number of nodes
2. Space: `O(h)`, where h is the tree height (recursion depth)

## Approach 2 - Stack - DFS
1. Initialize stack with `(root, path)`
2. While stack is not empty:
    - Pop `(node, path)`
    - If the node is leaf, add `path` to result
    - PUsh right and left children with updated paths

**Time and Space Complexity**: similar to approach 1

## Approach 3- Queue - BFS
1. Initialize queue with `(root, path)`
2. While the queue is not empty:
    - Dequeue `(node, path)`, if node is a leaf, add `path` to results
    - Enqueue **left and right children** with updated paths

**Time and Space Complexity**
1. Time: `O(n)`, where `n` is number of nodes
2. Space: `O(w)`, where `w` is the tree height (recursion depth)

