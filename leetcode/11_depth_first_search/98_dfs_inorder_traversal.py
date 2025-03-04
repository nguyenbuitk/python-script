from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isValidBST(root: Optional[TreeNode]) -> bool:
    preVal = float('-inf')
    def dfs(node):
        nonlocal preVal
        if not node:
            return True
        if not dfs(node.left):
            return False
        if node.val <= preVal:
            return False
        preVal = node.val
        return dfs(node.right)
    
    return dfs(root)

root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(27)
root.right.right = TreeNode(56)
print(isValidBST(root))