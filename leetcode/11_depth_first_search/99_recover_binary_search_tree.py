from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: TreeNode):
    res = []  # store two swapped node value
    arr = []
    current_node, stack, preVal = root,  [], float('-inf')
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        res.append(current_node.val)
        if current_node.val <= preVal:
            if not arr:
                arr.append(preVal)
                arr.append(current_node.val)
            else:
                arr.pop()
                arr.append(current_node.val)
                break
        preVal = current_node.val
        current_node = current_node.right
    print(res)
    print("two position: ", arr)
    
    current_node, stack = root, [] 
    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        if current_node.val == arr[0]:
            current_node.val = arr[1]
        elif current_node.val == arr[1]:
            current_node.val = arr[0]
            return
        current_node = current_node.right

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
