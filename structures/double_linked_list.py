class DLinkedNode:
  def __init__(self, value):
    self.next = None
    self.prev = None
    self.value = value

class DLinkedList:
  def is_empty(self):
    return self.size == 0

  def append(self, value):
    node = DLinkedNode(value)
    if self.tail is None:
      self.tail = node
      self.head = node
    else:
      node.prev = self.tail
      self.tail.next = node
      self.tail = node
  
  def prepend(self, value):
    node = DLinkedNode(value)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head.prev = node