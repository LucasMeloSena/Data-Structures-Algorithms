class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None


class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}

    self.left = Node(0, 0)
    self.right = Node(0, 0)

    self.left.next = self.right
    self.right.prev = self.left

  def get(self, key: int) -> int:
    if key in self.cache:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.remove(self.cache[key])

    self.cache[key] = Node(key, value)
    print(self.cache[key])  # debug
    self.insert(self.cache[key])

    if len(self.cache) > self.capacity:
      last_node = self.right.prev
      self.remove(last_node)
      del self.cache[last_node.key]

  def insert(self, node: Node) -> None:
    head, _next = self.left, self.left.next
    head.next = _next.prev = node
    node.prev = head
    node.next = _next

  def remove(self, node: Node) -> None:
    prev, _next = node.prev, node.next
    prev.next = _next
    _next.prev = prev
