from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isValidBSTDebug(root: Optional[TreeNode]) -> bool:
    preVal = float('-inf')
    stack = []
    
    current_node = root
    while stack or current_node:
        while current_node:
            stack.append(current_node)        
            print(f"In while loop, curent_node = {current_node.val}")
            current_node = current_node.left
        print("Current stack before pop: ")
        for node in stack:
            print(f"{node.val}", end = " ")
        print("")
        current_node = stack.pop()
        preVal = current_node.val
        current_node = current_node.right

        print(f"node just poped: {current_node.val}")
        current_node = current_node.right
        print(f"current node after pop(): {current_node.val if current_node else current_node}")
        print("")
        # if current_node.val <= preVal:
        #    return False
        # preVal = current_node.val
    return True
        
def isValidBST(root: Optional[TreeNode]) -> bool:
    preVal = float('-inf')
    stack = []
    
    current_node = root
    while stack or current_node:
        while current_node:
            stack.append(current_node)        
            current_node = current_node.left
        current_node = stack.pop()
        if current_node.val <= preVal:
           return False
        preVal = current_node.val
        current_node = current_node.right

    return True

root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(25)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(22)
root.right.right = TreeNode(56)
print(isValidBST(root))