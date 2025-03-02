class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            if left and right:
                return min(left, right) + 1
            
            if not left and not right:
                return 1
            
        return height(root)

"""
Ta sẽ kiểm tra cây ví dụ sau:

        3
       / \
      9   20
         /  \
        15   7
🔥 DFS sẽ duyệt theo thứ tự sau:

dfs(3)
    left = dfs(9) 
        left = dfs(None) = 0
        right = dfs(None) = 0
        → Trả về 1 (vì 9 không có con).
        
    right = dfs(20)
        left = dfs(15)
            return 1
        right = dfs(7)
            return 1
        return 2 
    return min(left, right) + 1 = 2
    

Giả sử sau:
        1
       / 
      2  
     / 
    3   
   /
  4   
dfs(1)
    left = dfs(2) = 3
        left = dfs(3) = 2
            left = dfs(4) = 1
                left = None
                right = None
                return 1 
            right = dfs(None) = 0
            return max(1,0) + 1 = 2
           
        right = None
        return 3
    return 4
"""
