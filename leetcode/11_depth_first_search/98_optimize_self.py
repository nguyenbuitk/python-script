from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, minVal, maxVal):
            if not node:
                return True
            # print(f"Current value passed: node: {node.val}, parent: {parent.val}, isLeft: {isLeftofParent}, minVal: {minVal}, maxVal: {maxVal} ")
            if node.val > maxVal or node.val < minVal:
                return False
            
            
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)
        
        return dfs(root, float('-inf'), float('inf'))
root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(27)
root.right.right = TreeNode(56)
solution = Solution()
print(solution.isValidBST(root))