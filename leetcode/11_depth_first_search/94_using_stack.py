class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    result, stack = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)
print(inorderTraversal(root))

# Constructed binary tree is
#          1
#        /   \
#      2      3
#    /  \
#  4     5

'''
1. Starting at Root (Node 1): current = 1
Push 1 to the stack. Stack S = [1]
Move current to the left child: current = 2

2. At Node 2:
Push 2 to the stack. Stack S = [2, 1]
Move current to the left child: current = 4

3. At Node 4:
Push 4 to the stack. Stack S = [4, 2, 1]
Move current to the left child: current = NULL (Node 4 has no left child)

4. current is NULL:
Pop 4 from the stack. Stack S = [2, 1]
Print 4
Move current to the right child of Node 4: current = NULL (Node 4 has no right child)

5. Repeat with current = NULL:
Pop 2 from the stack. Stack S = [1]
Print 2
Move current to the right child of Node 2: current = 5

6. At Node 5:
Push 5 to the stack. Stack S = [5, 1]
Move current to the left child: current = NULL (Node 5 has no left child)

7. current is NULL:
Pop 5 from the stack. Stack S = [1]
Print 5
Move current to the right child of Node 5: current = NULL (Node 5 has no right child)

8. Repeat with current = NULL:
Pop 1 from the stack. Stack S = []
Print 1
Move current to the right child of Node 1: current = 3

9. At Node 3:
Push 3 to the stack. Stack S = [3]
Move current to the left child: current = NULL (Node 3 has no left child)

10. current is NULL:
Pop 3 from the stack. Stack S = []
Print 3
Move current to the right child of Node 3: current = NULL (Node 3 has no right child)
'''