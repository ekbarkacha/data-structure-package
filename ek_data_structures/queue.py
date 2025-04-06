class Queue:
    def __init__(self, max_size = float('inf'), queue = None):
        if queue is None:
            queue = []
        self.queue = queue
        self.max_size = max_size

    def enqueue(self, new_element):
        """Adds a new element to the rear of the queue."""
        if len(self.queue) < self.max_size:
            self.queue.append(new_element)
        else:
            raise OverflowError("Queue is full, cannot enqueue element")

    def dequeue(self):
        """Removes and returns the first element of the queue."""
        if len(self.queue) > 0:
          first_element = self.queue[0]
          self.queue=self.queue[1:]
          return first_element
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def peek(self):
        """Returns the first element without removing it."""
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            raise IndexError("Queue is empty, cannot peek")

    def front(self):
        """Returns the first element without removing it."""
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            raise IndexError("Queue is empty, cannot access front element")

    def rear(self):
        """Returns the rear (last) element of the queue without removing it."""
        if len(self.queue) > 0:
            return self.queue[len(self.queue)-1]
        else:
          raise IndexError("Queue is empty, cannot access rear element")

    
    def is_full(self) -> bool:
        """Checks if the queue is full."""
        return len(self.queue) == self.max_size

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def display_queue(self):
        """Displays the current elements in the queue."""
        print(self.queue)

