# Easy
## 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
A binary tree is height-balanced if the depth of the two subtrees of every node never differs by more than 1.

Input: root = [3,9,20,null,null,15,7]
Output: true

Explanation:
The tree is balanced since for every node, the height difference between
left and right subtrees is at most 1.
```
        3
       / \
      9  20
         /  \
        15   7
```

# Key Idea
## Approach 1
1. Base Case: If the node is `None`, return height `0`
2. Recursive Case:
    - Compute the height of left subtree: `left_height = dfs(root.left)`
    - Compute the height of right subtree: `right_height = dfs(root.right)`
    - If `abs(left_height - right_height) > 1`, return `-1`
    - Return the height of the current node: `1 + max(left_height, right_height)`
3. If `dfs(root) == -1`, return `False`, else return `True`

Ta sẽ kiểm tra cây ví dụ sau:
```
        3
       / \
      9   20
         /  \
        15   7
```
🔥 DFS sẽ duyệt theo thứ tự sau:
```
dfs(9) → Trả về 1 (vì 9 không có con).
dfs(15) → Trả về 1 (vì 15 không có con).
dfs(7) → Trả về 1 (vì 7 không có con).
dfs(20):
Tính cây con trái (15): Chiều cao = 1.
Tính cây con phải (7): Chiều cao = 1.
Không mất cân bằng → Trả về 2.
dfs(3):
Tính cây con trái (9): Chiều cao = 1.
Tính cây con phải (20): Chiều cao = 2.
Chênh lệch |1 - 2| ≤ 1 → Cân bằng → Trả về 3.
Kết quả: True (Cây cân bằng).
```

Tại sao trả về -1 giúp tối ưu hóa?
Giả sử cây mất cân bằng:
```
        1
       / 
      2  
     / 
    3   
   /
  4  
```
```
dfs(4) → Trả về 1.
dfs(3):
Tính cây con trái (4): Chiều cao = 1.
Cây con phải = None → Chiều cao = 0.
Chênh lệch |1 - 0| ≤ 1 → Trả về 2.
dfs(2):
Cây con trái (3): Chiều cao = 2.
Cây con phải = None → Chiều cao = 0.
Chênh lệch |2 - 0| > 1 → Trả về -1 (mất cân bằng).
dfs(1):
Cây con trái (2) đã trả về -1 → Ngay lập tức trả về -1
```

## Approach 2 - Stack (also DFS)
1. Use a **dictionary** to store the height of nodes
2. Push nodes into the stack while processing left and right children first
3. Compute height differences while backtracking
4. If any node has `abs(left_height - right_height) > 1` -> return `False`

## Approach 3 - Queue
1. Use a **queue** to store nodes
2. For each node, compute the **height of its left and right subtree**
3. If violate condition, return `False`, else return `True`