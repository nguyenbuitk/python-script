class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []
    stack, res = [], []
    current_level, added_level = -1, -1
    current_node, level = root, 0
    while current_node or stack:
        while current_node:
            print(f"current node: {current_node.val}")
            print(f"current level: {level}")
            if level >= len(res):
                res.append(current_node.val)
            stack.append((current_node, level))
            current_node, level = current_node.right, level + 1

        current_node, level = stack.pop()
        print(f"current node after poped: {current_node.val}")
        print(f"current level after poped: {level}")
        current_node, level = current_node.left, level + 1
    print(res)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
rightSideView(root)
