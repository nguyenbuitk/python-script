from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: TreeNode):
    current_node, stack, preVal = root,  [], float('-inf')
    preNode, firstNode, secondNode = None, None, None
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        if current_node.val <= preVal:
            if not firstNode:
                firstNode = preNode
                secondNode = current_node
            else:
                secondNode = current_node
                break

        preVal = current_node.val
        preNode = current_node
        current_node = current_node.right
    temp = firstNode.val
    firstNode.val = secondNode.val
    secondNode.val = temp

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
