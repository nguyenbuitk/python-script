from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(root: Node):
    res = root
    if not root:
        return None
    queue = deque([root])
    while queue:
        level_size = len(queue)
        preNode = queue.popleft()
        
        if preNode.left:
            queue.append(preNode.left)
        if preNode.right:
            queue.append(preNode.right)
        for _ in range(1, level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            preNode.next = node
            preNode = node
        preNode.next = None
    return res
root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(7))
connect(root)
print(root.left.left.next.next.next.val)
