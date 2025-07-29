from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
  ahead = head
  while ahead and ahead.next:
     ahead = ahead.next.next
     head = head.next
  return head