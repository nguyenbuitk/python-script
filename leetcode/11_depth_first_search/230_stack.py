from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def kthSmallest(root: TreeNode, k: int):
    # dfs inorder traversal
    order = 1
    stack = []
    current_node = root
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        print(f"current node: {current_node.val}, order = {order}")
        if order == k:
            return current_node.val
        
        order += 1
        
        current_node = current_node.right
    
        
        
    return False


root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(22)
root.right.right = TreeNode(56)
print(kthSmallest(root, 6))