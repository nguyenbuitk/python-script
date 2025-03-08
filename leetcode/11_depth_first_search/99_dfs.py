from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: TreeNode):
    preNode, firstNode, secondNode = None, None, None

    def dfs(node):
        nonlocal preNode, firstNode, secondNode
        if not node:
            return
        dfs(node.left)
        if preNode and node.val <= preNode.val:
            if not firstNode:
                firstNode=preNode
            secondNode = node
        preNode = node
        dfs(node.right)
    
    dfs(root)
    firstNode.val, secondNode.val = secondNode.val, firstNode.val
    
    
#root = TreeNode(32)
#root.left = TreeNode(26)
#root.right = TreeNode(22)
#root.left.left = TreeNode(19)
#root.left.left.right = TreeNode(47)
#root.right.right = TreeNode(56)
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
recoverTree(root)
