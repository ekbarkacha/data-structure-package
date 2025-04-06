class Stack:
    
    def __init__(self, para=None):
        if para is None:
            para = []
        self.stack = para

    def push(self,newElement)->None:
      """Add the new element to the stack"""
      self.stack.append(newElement)

    
    def pop(self):
        """Remove the last element from the stack by slicing if it's not empty"""
        if self.is_empty():
          raise IndexError("Cannot pop from an empty stack")
        else:
          last_in = self.stack[len(self.stack) - 1]
          self.stack = self.stack[:-1]
          return last_in

    def top(self):
      """Return the top element without removing it if the stack is not empty"""
      if not self.is_empty():
        last_in = self.stack[len(self.stack)-1]
        return last_in
      else:
        raise IndexError("Cannot access top of an empty stack")

    def display_stack(self)->None:
      """Display the current elements in the stack"""
      print(self.stack)

    def is_empty(self) -> bool:
      """Return True if the stack is empty, otherwise False"""
      return len(self.stack) == 0

    def size(self) -> int:
      """Return the number of elements in the stack"""
      return len(self.stack)