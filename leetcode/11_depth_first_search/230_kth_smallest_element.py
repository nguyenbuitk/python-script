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
        print(f"{node.val}, current = {current}")
        if node.left: 
            m = dfs(node.left) 
            if m != None:
                return m
        if current == k:
            return node.val
        current += 1
        if node.right: 
            n =  dfs(node.right)
            if n != None:
                return n
    res = dfs(root)
    return False if  res == None else res

root = TreeNode(31)
root.left = TreeNode(30)
root.right = TreeNode(48)

root.left.left = TreeNode(3)
root.right.left = TreeNode(38)
root.right.right = TreeNode(49)

root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(16)
root.right.left.left = TreeNode(35)
root.right.left.right = TreeNode(47)

root.left.left.right.left = TreeNode(2)
root.left.left.right.right = TreeNode(15)
root.right.left.left.left = TreeNode(33)
root.right.left.left.right = TreeNode(37)
root.right.left.right.left = TreeNode(39)

root.left.left.right.left.left = TreeNode(1)
root.left.left.right.left.right = TreeNode(5)
root.right.left.left.left.left = TreeNode(32)
root.right.left.left.left.right = TreeNode(34)
root.right.left.left.right.left = TreeNode(36)
root.right.left.right.left.right = TreeNode(43)

root.left.left.right.left.right.left = TreeNode(4)
root.left.left.right.left.right.right = TreeNode(11)
root.right.left.right.left.right.left = TreeNode(40)
root.right.left.right.left.right.right = TreeNode(46)

root.left.left.right.left.right.right.left = TreeNode(7)
root.left.left.right.left.right.right.right = TreeNode(14)
root.right.left.right.left.right.left.right = TreeNode(41)
root.right.left.right.left.right.right.left = TreeNode(44)

root.left.left.right.left.right.right.left.left = TreeNode(6)
root.left.left.right.left.right.right.left.right = TreeNode(10)
root.left.left.right.left.right.right.right.left = TreeNode(13)
root.right.left.right.left.right.left.right.right = TreeNode(42)
root.right.left.right.left.right.right.left.right = TreeNode(45)

root.left.left.right.left.right.right.left.left.left = TreeNode(8)
root.left.left.right.left.right.right.left.left.right = TreeNode(12)
root.left.left.right.left.right.right.left.left.left.left = TreeNode(9)

print(kthSmallest(root, 1))