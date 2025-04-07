from .queue import Queue

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinaryTree:

  def __init__(self):
    self.root = None

  def insert(self, data):
    if not isinstance(data, (int,float, str)):
        raise TypeError("Data type is not supported for insertion. Only int,float and str are supported")
    elif self.root is None:
        self.root = Node(data)
    else:
      # Start from the root and find the correct position for the new node
      node = self.root
      while True:
        # If the data is smaller, move to the left child
        if data < node.data:
          if node.left is None:
            node.left = Node(data)
            break
          else:
            node = node.left
        # If the data is larger, move to the right child
        elif data > node.data:
          if node.right is None:
            node.right = Node(data)
            break  
          else:
            node = node.right

  # BFS for binary tree (using queue from my own class Queue)
  def search(self, data) -> bool:

    if self.root is None:
        return False
    
    queue = Queue(queue=[self.root])  # Initialize queue with root first
    
    while not queue.is_empty():
        node = queue.dequeue()  # Dequeue a node
        if node.data == data:
            return True
        
        # Enqueue left and right children if they exist
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    
    return False  # Return False if the target is not found


  def delete(self, data):
    if self.root is None:
      raise ValueError("The tree is empty. Nothing to delete.")
    node = self.root
    parent = None

    while node:
      if data < node.data:
        parent = node
        node = node.left
      elif data > node.data:
        parent = node
        node = node.right
      else:
        # Node to be deleted found
        # Case 1: Node has no children
        if node.left is None and node.right is None:
          if parent is None:  # The root node is the only node in the tree
              self.root = None
          elif parent.left == node:
              parent.left = None
          else:
              parent.right = None

        # Case 2: Node has one child
        elif node.left is None:
            if parent is None:  # The root node has only one child
                self.root = node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right

        elif node.right is None:
            if parent is None:  # The root node has only one child
                self.root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

        # Case 3: Node has two children
        else:
            # Find the in-order successor (the smallest node in the right subtree)
            successor_parent = node
            successor = node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Copy the successor's data to the current node
            node.data = successor.data

            # Delete the successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return  # Node has been deleted, exit the function

    # node was not found
    raise ValueError(f"Node with data {data} was not found in the tree.")


  # Inorder Traversal
  def in_order(self):
    # Create an empty stack to simulate recursion stack
    stack = []
    current_node = self.root

    # Traverse the tree iteratively
    while stack or current_node:
      # Reach the leftmost node
      while current_node:
          stack.append(current_node)
          current_node = current_node.left
      
      # Pop from stack and process the node
      current_node = stack.pop()
      print(current_node.data, end=" ")
      
      # Move to the right subtree
      current_node = current_node.right

    print()

  # Preorder Traversal
  def pre_order(self):
    stack = []
    current_node = self.root

    while stack or current_node:
        if current_node:
            # Process the current node (Root node)
            print(current_node.data, end=" ")
            stack.append(current_node)
            current_node = current_node.left 
        else:
            # If the left child is None, pop from stack and go to the right child
            current_node = stack.pop()
            current_node = current_node.right

    print()

  # Postorder Traversal
  def post_order(self):
    stack = []
    current_node = self.root
    last_visited_node = None

    while stack or current_node:
        if current_node:
            stack.append(current_node)
            current_node = current_node.left
        else:
            peek_node = stack[-1]
            # If right child exists and we are not yet processed it
            if peek_node.right and last_visited_node != peek_node.right:
                current_node = peek_node.right
            else:
                # Process the node
                print(peek_node.data, end=" ")
                last_visited_node = stack.pop()
                
    print()