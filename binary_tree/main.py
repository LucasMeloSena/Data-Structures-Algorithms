from typing import List
from collections import deque

class Node:
  def __init__(self, val: int) -> None:
    self.val = val
    self.left = None
    self.right = None
    
class BinaryTree:
  def __init__(self) -> None:
    self.root = None
    
  def insert(self, val: int):
    if self.root is None:
      self.root = Node(val)
    else:
      self.__insert_recursive(val, self.root)
    
  def __insert_recursive(self, val: int, node: Node):
    if (val < node.val):
        if node.left is None:
          node.left = Node(val)
        else:
          self.__insert_recursive(val, node.left)
    else:
      if node.right is None:
        node.right = Node(val)
      else:
        self.__insert_recursive(val, node.right)
        
  def search(self, val: int):
    return self.__search_recursive(val, self.root)
  
  def __search_recursive(self, val: int, node: Node):
    if node is None:
      return False
    if node.val == val:
      return True
    elif val < node.val:
      return self.__search_recursive(val, node.left)
    else:
      return self.__search_recursive(val, node.right)
    
  def dfs(self, val: int):
    return self.__dfs_recursive(val, self.root)
  
  def __dfs_recursive(self, val: int, node: Node):
    if node is None:
      return False
    if node.val == val:
      return True
    
    if self.__dfs_recursive(val, node.left):
      return True
    if self.__dfs_recursive(val, node.right):
      return True
    
  def preorder_traversal(self):
    result = []
    self.__preorder_recursive(self.root, result)
    return result
  
  def __preorder_recursive(self, node: Node, result: List[int]):
    if node is not None:
      result.append(node.val)
      self.__preorder_recursive(node.left, result)
      self.__preorder_recursive(node.right, result)
      
  def inorder_traversal(self):
    result = []
    self.__inorder_recursive(self.root, result)
    return result
  
  def __inorder_recursive(self, node: Node, result: List[int]):
    if node is not None:
      self.__inorder_recursive(node.left, result)
      result.append(node.val)
      self.__inorder_recursive(node.right, result)
  
  def postorder_traversal(self):
    result = []
    self.__postorder_recursive(self.root, result)
    return result
  
  def __postorder_recursive(self, node: Node, result: List[int]):
    if node is not None:
      self.__postorder_recursive(node.left, result)
      self.__postorder_recursive(node.right, result)
      result.append(node.val)
      
  def bfs(self, val: int):
    if self.root is None:
      return False
    
    queue = deque()
    queue.append(self.root)
    
    while queue:
      node = queue.popleft()
      if node.val == val:
        return True
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      return False
    
tree = BinaryTree()
values = [5, 3, 1, 10, 7, 15]
for val in values:
    tree.insert(val)

print(tree.search(7))
print(tree.search(14))
print(tree.search(10))
print(tree.search(18))

print(tree.dfs(15))