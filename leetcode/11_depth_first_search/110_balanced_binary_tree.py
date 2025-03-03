class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalance(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  # if detect tree is not balanced, return -1
            
            return max(left, right) + 1            
        
        return dfs(root) != -1  # if contain -1, return not balanced
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(1), TreeNode(2))

solution = Solution()
print(solution.isBalance(root))