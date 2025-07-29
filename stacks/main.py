class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Stack:
  def __init__(self):
    self.head = None
    self._size = 0
    self.min_stack = None
    
  def push(self, item):
    node = Node(item)
    node.next = self.head
    self.head = node

    if self.min_stack is None or item <= self.min_stack.value:
      min_node = Node(item)
      min_node.next = self.min_stack
      self.min_stack = min_node

    self._size += 1
    
  def pop(self):
    if not self._size:
      raise IndexError("Empty stack")
    
    node_to_pop = self.head
    self.head = node_to_pop.next
    self._size -= 1
    
    if node_to_pop.value == self.min_stack.value:
      self.min_stack = self.min_stack.next
    
    return node_to_pop.value
  
  def peek(self):
    if not self._size:
      raise IndexError("Empty stack")
    
    return self.head.value
  
  def size(self):
    return self._size
  
  def get_min(self):
    if not self._size:
      raise IndexError("Empty stack")
    
    return self.min_stack.value