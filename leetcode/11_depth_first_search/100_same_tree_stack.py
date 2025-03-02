from collections import deque, stack

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode):
    stack = [(p,q)]
    while stack:
      node_p, node_q = stack.pop()
      if not node_q and not node_p:
        continue
      if not node_q or not node_p or node_q.val != node_p.val:
        return False
      stack.append((node_p.left, node_q.left))
      stack.append((node_p.right, node_q.right))

    return True

