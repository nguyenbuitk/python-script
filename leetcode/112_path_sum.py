class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(node, target):
            if node.val == target:
                return True
            if not node:
                return 0
            left = dfs(node.left, target - node.val)
            if left: return True
            right = dfs(node.right, target - node.val)
            return left or right
        return dfs(root, targetSum)


"""
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1

dfs(5, 22):
    left = dfs(4, 17) = 1
        left = dfs(11, 13) = 1
            left = dfs(7,2) = 0
                left = dfs(None, -5) = 0
                right = dfs(None, -5) = 0
            right = dfs(2,2) = 1
                return True
            return left or right =1
        right = dfs(None, 13) = 0
            return 0
        return 1
    right = dfs(8, 17)


        1
       / 
      2

dfs(1, 1):
    left = dfs(4, 17) = 1
        left = dfs(11, 13) = 1
            left = dfs(7,2) = 0
                left = dfs(None, -5) = 0
                right = dfs(None, -5) = 0
            right = dfs(2,2) = 1
                return True
            return left or right =1
        right = dfs(None, 13) = 0
            return 0
        return 1
    right = dfs(8, 17)
"""