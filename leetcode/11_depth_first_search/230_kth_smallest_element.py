from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def kthSmallest(root: TreeNode, k: int):
    # dfs inorder traversal
    current = 1
    def dfs(node):
        nonlocal current
        if node.left: 
            return dfs(node.left)
        print(f"{node.val}, current = {current}")
        if current == k:
            return node.val
        current += 1
        if node.right: 
            return dfs(node.right)
        
    return dfs(root)


root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(22)
root.right.right = TreeNode(56)
print(kthSmallest(root, 2))