class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:

    def __init__(self):
      self.head = None

    def insert_start(self, item):
      """Add a node at the start of the linked list (head)"""
      new_node = Node(item)
      new_node.next = self.head
      self.head = new_node

    def insert_after(self, item, index):
        """Insert a node at a specific position in the list, shifting elements as needed."""
        node = Node(item)
        temp = self.head
        i = 0  
        # Finding the index
        while temp and i < index:
            temp = temp.next
            i += 1
        if temp is None:
            raise IndexError(f"Index {index} doesn't exist.")
        else:
          node.next = temp.next
          temp.next = node

    def insert_end(self, item):
      """Add a node at the end of the linked list"""
      new_node = Node(item)
      if not self.head:
        self.head = new_node
      else:
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node


    def delete_item(self, index):
      if index<0:
        raise ValueError(f"The index {index} cannot be negative.")
      elif self.head is None:
        raise IndexError("Nothing to delete; linked list is empty.")
      elif index == 0:
        #Remove the head node of the linked list.
        self.head = self.head.next
      else:
        #Remove a node from a specific position in the list.
        temp = self.head
        i = 0
        while i<index and temp.next:
          prev = temp
          temp = temp.next
          i+=1
        if i == index:
          prev.next = temp.next
        else:
          raise IndexError(f"Index {index} doesn't exist.")

    def display(self):
      """Visit each node in the linked list starting from the head and display its data until the end of the list is reached."""
      node = self.head
      while node:
          print(node.data, end=" -> ")
          node = node.next
      print("None")

    def traverse(self):
      """Visit each node in the linked list starting from the head and display its data until the end of the list is reached."""
      node = self.head
      while node:
          print(node.data, end=" -> ")
          node = node.next
      print("None")

    def search(self, item) -> bool:
      """Look for a node with a specific value, and return true if it exist else false."""
      node = self.head
      index = 0
      while node:
          if node.data == item:
              return True
          node = node.next
          index += 1
      return False

    def get_length(self)-> int:
      """counting the number of nodes."""
      count = 0
      node = self.head
      while node:
          count += 1
          node = node.next
      return count

    def access(self, index):
      """Accessing data of a specific node given the index"""
      node = self.head
      count = 0
      while node:
          if count == index:
              return node.data
          node = node.next
          count += 1
      return None

    def update(self, index, new_data):
      """Update the data of a specific node by first finding it and then modifying its data."""
      node = self.head
      count = 0
      while node:
          if count == index:
              node.data = new_data
              return
          node = node.next
          count += 1
      raise IndexError("Index out of bounds.")

    