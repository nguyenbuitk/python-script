from collections import deque

def isCousins(root, x, y):
    queue = deque([(root, None)])
    while queue:
        l = len(queue)
        node_parent = []
        for _ in range(l):
            node, parent = queue.popleft()
            if node.val == x or node.val == y:
                node_parent.append(parent)
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        if len(node_parent) == 2 and node_parent[0] != node_parent[1]:
            return True
    return False
            
            
    