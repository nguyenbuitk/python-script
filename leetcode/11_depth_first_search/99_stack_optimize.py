from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: TreeNode):
    stack = []
    preNode, firstNode, secondNode = None, None, None
    current_node = root
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        
        current_node = stack.pop()
        if preNode and current_node.val <= preNode.val:
            if not firstNode:
                firstNode = preNode
            secondNode = current_node
        
        preNode = current_node
        current_node = current_node.right

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
