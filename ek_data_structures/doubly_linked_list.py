class Node:
    def __init__(self, item):
        self.prev = None
        self.data = item
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, item):
        """Insert a new node at the beginning of the list."""
        new_node = Node(item)
        new_node.next = self.head

        # If the list is not empty, update the previous head's previous pointer to the new node.
        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insert_at(self, index, item):
        """Insert a new node at a specific index."""
        if index < 0:
            raise ValueError(f"Index ({index}) cannot be negative")

        new_node = Node(item)
        i = 0
        temp = self.head

        # If inserting at the head
        if index == 0:  
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index > 0 and self.head is None:
            raise IndexError(f"Cannot insert at index {index} since list is empty")

        else:
            while i < index and temp:
                i += 1
                temp = temp.next

            if i == index:
                new_node.prev = temp.prev
                new_node.next = temp

                if temp.prev:
                    temp.prev.next = new_node
                temp.prev = new_node
            else:
                raise IndexError(f"The index {index} is out of range")

    def insert_at_end(self, item):
        """Insert a new node at the end of the list."""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            new_node.prev = temp
            temp.next = new_node

    def delete_item(self, index):
        """Delete a node at a specific index."""
        if index < 0:
            raise ValueError(f"The index {index} cannot be negative.")
        elif self.head is None:
            raise IndexError("Nothing to delete, the list is empty.")

        # If deleting the head node
        if index == 0:  
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
        else:
            temp = self.head
            i = 0
            while i < index and temp:
                temp = temp.next
                i += 1

            if i == index:
                if temp.next:
                    temp.next.prev = temp.prev
                if temp.prev:
                    temp.prev.next = temp.next
            else:
                raise IndexError(f"Index {index} doesn't exist.")

    def display(self):
        """Display the list in a human-readable format."""
        node = self.head
        while node:
            print(node.data, end=" <--> ")
            node = node.next
        print('None')

    def search(self, item):
        """Search for a specific item in the list and return True if the item is found, False otherwise.
        """
        node = self.head
        while node:
            if node.data == item:
                return True
            node = node.next
        return False

    def get_length(self):
        """Get the length of the list by counting the number of nodes."""
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count  # Return the total number of nodes in the list

    def access(self, index):
        """Access the data of the node at the given index."""
        if index < 0:
            raise ValueError(f"Index ({index}) cannot be negative") 
        node = self.head
        count = 0
        while node:
            if count == index:
                return node.data
            node = node.next
            count += 1
        raise IndexError(f"Index {index} out of bounds.")

    def update(self, index, new_data):
        """Update the data of a node at a specific index."""
        if index < 0:
            raise ValueError(f"Index ({index}) cannot be negative")
        node = self.head
        count = 0
        while node:
            if count == index:
                node.data = new_data
                return
            node = node.next
            count += 1
        raise IndexError(f"Index {index} out of bounds.")
