class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_start(self, value):
    new_node = Node(value)
    new_node.next = self.head
    if (self.head):
      self.head.prev = new_node
    else:
      self.tail = new_node
    self.head = new_node

  def add_to_end(self, value):
    new_node = Node(value)
    new_node.prev = self.tail
    if (self.tail):
      self.tail.next = new_node
    else:
      self.head = new_node
    self.tail = new_node

  def remove_from_start(self):
    if self.head is None:
      return None
    
    removed_node = self.head
    self.head = removed_node.next
    if (self.head):
      self.head.prev = None
    else:
      self.tail = None
    return removed_node.value

  def remove_to_end(self):
    if self.tail is None:
      return None
    
    removed_node = self.tail
    self.tail = removed_node.prev
    if (self.tail):
      self.tail.next = None
    else:
      self.head = None
    return removed_node.value
  
def test_doubly_linked_list():
    dll = DoublyLinkedList()

    print("== Teste: adicionar ao início ==")
    dll.add_to_start(3)
    dll.add_to_start(2)
    dll.add_to_start(1)
    print_list(dll)  # Esperado: [1, 2, 3]

    print("== Teste: adicionar ao fim ==")
    dll.add_to_end(4)
    dll.add_to_end(5)
    print_list(dll)  # Esperado: [1, 2, 3, 4, 5]

    print("== Teste: remover do início ==")
    removed = dll.remove_from_start()
    print("Removido do início:", removed)
    print_list(dll)  # Esperado: [2, 3, 4, 5]

    print("== Teste: remover do fim ==")
    removed = dll.remove_to_end()
    print("Removido do fim:", removed)
    print_list(dll)  # Esperado: [2, 3, 4]

    print("== Teste: remover todos ==")
    dll.remove_from_start()
    dll.remove_from_start()
    dll.remove_from_start()
    print_list(dll)  # Esperado: []

    print("== Teste: remover de lista vazia ==")
    print("Removido do início:", dll.remove_from_start())  # Esperado: None
    print("Removido do fim:", dll.remove_to_end())  
    
def print_list(dll):
    """Imprime os valores da lista do início ao fim"""
    current = dll.head
    values = []
    while current:
        values.append(current.value)
        current = current.next
    print("Lista:", values)

test_doubly_linked_list()