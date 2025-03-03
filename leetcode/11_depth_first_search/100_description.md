# Easy
## 100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Explanation:
Both trees have the same structure and identical node values.
```
  1         1
 / \       / \
2   3     2   3
```
# Key Idea
## Approach 1: DFS
1. Base case:
    - If both nodes are `None`, return `True`
    - If only one node is `None`, or values are different, return `False`
2. Recusive Call:
    - Check the left subtree: `dfs(p.left, q.left)`
    - Check the right subtree: `dfs(p.right, q.right)`
3. Return `True` if check left `True` and check right `True`

## Approach 2: Stack - Also DFS

1. Instead of recursion, use a stack (LIFO) to traverse the tree simultaneously
2. Push pairs of node `(p, q)` into the stack
3. At each step:
    - Pop a pair `(node_p, node_q)` **pop right**
    - If both nodes are `None`, continue
    - If only one is `None` or values are different, return `False`
    - **Push left and right child pairs** into stack
    ```python
    stack.append((node_p.left, node_q.left))
    stack.append((node_p.right, node_q.right))
    ```

## Approach 3: BFS - Queue
1. Instead of DFS, use **BFS** with a queue (FIFO)
2. Compare each level of the tree before moving to the next
3. At each step
    - Dequeue a pair `(node_p, node_q)` **pop left**
    - If both are None, continue.
    - If only one is None or values are different, return False.
    - Enqueue left children `(p.left, q.left)`, and right children `(p.right, q.right)`

### Example 
```
        1
       / \
      2   3
     / \   \
    4   5   6
```
### **1️⃣ Stack (DFS - Depth-First Search)**
📌 **Uses LIFO (Last In, First Out)** → Processes **deepest nodes first**.  
#### **Stack Traversal (Preorder: Root → Left → Right)**
1. **Push root node `1`**
2. **Pop `1`, push `3`, push `2`**  (Push right child first to process left first)
3. **Pop `2`, push `5`, push `4`**
4. **Pop `4`** (No children)
5. **Pop `5`** (No children)
6. **Pop `3`, push `6`**
7. **Pop `6`** (No children)

### **2️⃣ Queue (BFS - Breadth-First Search)**
📌 **Uses FIFO (First In, First Out)** → Processes **all nodes at the current level before going deeper**. 
#### **BFS Traversal (Level Order: Left to Right)**
1. **Enqueue root node `1`**
2. **Dequeue `1`, enqueue `2`, enqueue `3`**
3. **Dequeue `2`, enqueue `4`, enqueue `5`**
4. **Dequeue `3`, enqueue `6`**
5. **Dequeue `4`** (No children)
6. **Dequeue `5`** (No children)
7. **Dequeue `6`** (No children)
