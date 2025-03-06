# Medium
## 199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

# Key Idea
## Approach 1 - BFS (Optimal)
1. Initialize a queue and start level-order traversal
2. At each levle, track the rightmost node
3. At the endof each level, add the last node of that level to the result
**Time and Space Complexity**
1. Time: `O(n)`
2. Space: `O(w)`

## Approach 2 - DFS (Recursive)
1. Use DFS (preorder traversal) starting from the root
2. At each level, add the first encounter node to the result
3. Recur for the right child first, then the left child
**Time and Space Complexity**
1. Time: `O(n)`
2. Space: `O(h)`

## Approach 3 - DFS (Stack Iterative)
1. Use a stack (`LIFO`) to perform iterative DFS
    - `stack = [(current_node, current_level)]`
2. Track the first node encountered at each depth
3. Process the right child first 
**Time and Space Complexity**
1. Time: `O(n)`
2. Space: `O(h)`

