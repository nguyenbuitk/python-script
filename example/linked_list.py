class ListNode:
  def __init__(self, data):
    self.val = data
    self.next = None

def detect_loop(head):
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True
  return False

node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(40)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

current = node1
if detect_loop(node1):
  print("Loop detected")
else:
  while current:
    print(current.val, end=" ->")
    current = current.next

