class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalance(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  # if detect tree is not balanced, return -1
            
            return max(left, right) + 1            
        
        return height(root) != -1  # if contain -1, return not balanced
    
"""
Ta sẽ kiểm tra cây ví dụ sau:

        3
       / \
      9   20
         /  \
        15   7
🔥 DFS sẽ duyệt theo thứ tự sau:

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


Tại sao trả về -1 giúp tối ưu hóa?
Giả sử cây mất cân bằng:
        1
       / 
      2  
     / 
    3   
   /
  4   
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
Cây con trái (2) đã trả về -1 → Ngay lập tức trả về -1 (không cần tính tiếp).
"""
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(1), TreeNode(2))

solution = Solution()
print(solution.isBalance(root))