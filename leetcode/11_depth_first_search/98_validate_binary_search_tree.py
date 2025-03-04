from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, parent, isLeftofParent, minVal, maxVal):
            if not node:
                return True
            print(f"Current value passed: node: {node.val}, parent: {parent.val}, isLeft: {isLeftofParent}, minVal: {minVal}, maxVal: {maxVal} ")
            if isLeftofParent:
                if node.val >= parent.val or node.val <= minVal:
                    return False
                
            if not isLeftofParent:
                if node.val <= parent.val or node.val >= maxVal:
                    return False
            
            return dfs(node.left, node, True, minVal, node.val) and dfs(node.right, node, False, node.val, maxVal)
        
        return dfs(root.left, root, True, float('-inf'), root.val) and dfs(root.right, root, False, root.val, float('inf'))

root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(27)
root.right.right = TreeNode(56)
solution = Solution()
print(solution.isValidBST(root))