from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def kthSmallest(root: TreeNode, k: int):
    current = 0  # Tracks the number of elements visited
    result = None  # Stores the k-th smallest element
    
    def dfs(node):
        nonlocal current, result
        if not node or result is not None:
            return
        
        # Inorder traversal: Left -> Node -> Right
        dfs(node.left)
        
        current += 1
        if current == k:
            result = node.val
            return
        
        dfs(node.right)
    
    dfs(root)
    return result if result is not None else False

root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(22)
root.right.right = TreeNode(56)
print(kthSmallest(root, 2))
