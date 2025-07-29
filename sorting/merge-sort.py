class Node:
  def __init__(self, val=0, next = None):
    self.val = val
    self.next = next

def find_middle(head):
  if (head is None):
    return head
  
  slow = head
  fast = head
  
  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
  return slow

def sorted_merge(left, right):
  if left is None:
    return right
  if right is None:
    return left
  
  if left.val <= right.val:
    result = left
    result.next = sorted_merge(left.next, right)
  else:
    result = right
    result.next = sorted_merge(left, right.next)
    
  return result

def merge_sort(head):
  if head is None or head.next is None:
    return head

  middle = find_middle(head)
  next_middle = middle.next
  middle.next = None
  left = merge_sort(head)
  right = merge_sort(next_middle)
  
  sorted_list = sorted_merge(left, right)
  return sorted_list

node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)
sorted_head = merge_sort(node_9)