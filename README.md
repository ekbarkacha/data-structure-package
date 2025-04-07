# Data Structure Package

This package provides implementations of several common data structures and their basic operations. The package includes:

- Array
- Stack
- Queue
- Linked List
- Doubly Linked List
- Binary Tree
- Graph

Each data structure is implemented with a set of core methods, providing users with the ability to manipulate and interact with the data structures in a direct way. Below is an overview of each data structure and the operations available.

## Table of Contents
1. [Array Class](#array-class)
2. [Stack Class](#stack-class)
3. [Queue Class](#queue-class)
4. [Linked List Class](#linked-list-class)
5. [Doubly Linked List Class](#doubly-linked-list-class)
6. [Binary Tree Class](#binary-tree-class)
7. [Graph Class](#graph-class)
8. [Installation](#installation)
9. [Usage](#usage)

---

## Array Class

The `Array` class provides basic operations on dynamic arrays, allowing for efficient management and manipulation of array data.

### Supported Operations:
- `length()` - Returns the number of elements in the array.
- `append(item)` - Adds an item to the end of the array.
- `insert(index, item)` - Inserts an item at a specific index.
- `remove(item)` - Removes the first occurrence of the item.
- `contains(item)` - Checks if an item exists in the array.
- `clear()` - Clears all elements in the array.
- `is_equal(other_array)` - Compares if two arrays are equal.
- `concatenate(other_array)` - Concatenates another array to the current one.
- `pop()` - Removes the last item from the array by default else you can specify index.
- `delete(index)` - Removes an item at a specific index.

### Example:
```python
arr = Array()
arr.append(10)
arr.append(20)
arr.insert(1, 15)
print(arr.length())  # Output: 3
arr.remove(15)
print(arr.contains(10))  # Output: True
```
For more detailed usage examples you can also check out the [array example notebook](./array_example.ipynb) .

---

## Stack Class

The `Stack` class provides a LIFO (Last In First Out) data structure to push and pop items.

### Supported Operations:
- `push(item)` - Adds an item to the top of the stack.
- `pop()` - Removes and returns the top item.
- `top()` - Returns the top item without removing it.
- `size()` - Returns the number of items in the stack.
- `is_empty()` - Checks if the stack is empty.
- `display_stack()` - Displays the elements in the stack.


### Example:
```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display_stack() #[10, 20, 30, 40]
print(s.top())    # Output: 40
s.pop()           # Output: 40
print(s.size())   # Output: 3
s.display_stack() #[10, 20, 30]
```
For more detailed usage examples you can also check out the [stack example notebook](./stack_example.ipynb) .

---

## Queue Class

The `Queue` class provides a FIFO (First In First Out) data structure with operations to add, remove, and inspect items in the queue.

### Supported Operations:
- `enqueue(item)` - Adds an item to the rear/end of the queue.
- `dequeue()` - Removes and returns the front item.
- `peek()` / front()` - Returns the front item without removing it.
- `rear()` - Returns the rear/end item.
- `is_full()` - Checks if the queue is full.
- `is_empty()` - Checks if the queue is empty.
- `display_queue()` - Displays the elements in the queue.

### Example:
```python
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40) 
q.display_queue() #[10, 20, 30, 40]
print(q.rear())  # Output: 40
q.dequeue()
q.display_queue() #[20, 30, 40]
print(q.front())  # Output: 20
```
For more detailed usage examples you can also check out the [queue example notebook](./queue_example.ipynb) .

---

## Linked List Class

The `LinkedList` class implements a single linked list with methods to add, remove, and access elements in the list.

### Supported Operations:
- `insert_start(item)` - Inserts an item at the beginning of the list.
- `insert_after(item, index)` - Inserts an item after a specific node.
- `insert_end(item)` - Inserts an item at the end of the list.
- `delete_item(index)` - Deletes the item at specific index.
- `display()` / `traverse()` - Displays the entire list.
- `search(item)` - Searches for an item in the list and returns True if it exist else False.
- `get_length()` - Returns the number of nodes in the list.
- `access(index)` - Accesses the node at a specific index.
- `update(index, item)` - Updates the node at a specific index with a new item.

### Example:
```python
ll = LinkedList()
ll.insert_start(10)
ll.insert_end(20)
ll.insert_after(15,0)
ll.display()  # Output: 10 -> 15 -> 20 -> None
```
For more detailed usage examples you can also check out the [linked_list example notebook](./linked_list_example.ipynb) .

---
## Doubly Linked List Class

The `DoublyLinkedList` class implements a doubly linked list with methods to add, remove, and access elements in the list. Each node here has references to both the previous and next nodes.

### Supported Operations:
- `insert_at_beginning(item)` - Inserts an item at the beginning of the list.
- `insert_at(index, item)` - Inserts an item at a specific index.
- `insert_at_end(item)` - Inserts an item at the end of the list.
- `delete_item(index)` - Deletes the item at a specific index.
- `display()` - Displays the entire list from start to end.
- `search(item)` - Searches for an item in the list and returns `True` if it exists, `False` otherwise.
- `get_length()` - Returns the number of nodes in the list.
- `access(index)` - Accesses the node at a specific index and returns its data.
- `update(index, item)` - Updates the node at a specific index with a new item.

### Example:
```python
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at(1, 15)
dll.display()  # Output: 10 <--> 15 <--> 20 <--> None
```

For more detailed usage examples you can also check out the [doubly_linked_list example notebook](./doubly_linked_list_example.ipynb) .

---

## Binary Tree Class

The `BinaryTree` class implements a binary tree, offering methods for traversal and modification of the tree.

### Supported Operations:
- `insert(item)` - Inserts an item into the tree.
- `search(item)` - Searches for an item in the tree returns True if exists else False.
- `delete(item)` - Deletes an item from the tree.
- `in_order()` - Traverses the tree in-order (left, root, right).
- `pre_order()` - Traverses the tree pre-order (root, left, right).
- `post_order()` - Traverses the tree post-order (left, right, root).

### Example:
```python
r"""
      3
    /   \
   1     4
    \
     2
     """
bt = BinaryTree()
bt.insert("3")
bt.insert("1")
bt.insert("2")
bt.insert("4")
bt.in_order()  # Output: 1 -> 2 -> 3 -> 4 (left root right)
bt.pre_order()  # Output: 3 -> 1 -> 2 -> 4 (root left right)
bt.post_order()  # Output: 2 -> 1 -> 4 -> 3 (left right root)
```
For more detailed usage examples you can also check out the [binary tree example notebook](./tree_example.ipynb) .

---

## Graph Class

The `Graph` class implements an **undirected graph** using an **adjacency list**. This class includes various methods for adding and removing vertices and edges, as well as performing DFS and BFS traversals.

### Supported Operations:
- `add_vertex(vertex)` - Adds a vertex to the graph.
- `add_edge(vertex1, vertex2)` - Adds an undirected edge between two vertices.
- `remove_vertex(vertex)` - Removes a vertex and all edges associated with it.
- `remove_edge(vertex1, vertex2)` - Removes the edge between two vertices.
- `has_edge(vertex1, vertex2)` - Checks if an edge exists between two vertices.
- `dfs(start_vertex, visited)` - Performs Depth-First Search from a starting vertex.
- `bfs(start_vertex)` - Performs Breadth-First Search starting from a given vertex.
- `find_path(start, end, path)` - Finds a path from start to end using DFS.
- `search(vertex)` - Searches for a vertex in the graph. Returns True if found, else False.
- `display_graph()` - Displays the adjacency list of the graph.

### Example:
```python
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.display_graph()
# Output:
# A: ['B']
# B: ['A', 'C']
# C: ['B']

g.dfs("A", visited=set())  # Output: A B C
g.bfs("A")  # Output: A B C
g.find_path("A", "C", path=[])  # Output: A -> B -> C
```

For more detailed usage examples, you can also check out the [graph example notebook](./graph_example.ipynb).

---

## Installation

To iinstall the package directly from PyPI using:

```bash
pip install ek-data-structures
```

---

## Usage

After installation, you can import the data structures into your Python code:

```python
from ek_data_structures import Array, LinkedList, Queue, Stack, BinaryTree

# Example usage
arr = Array()
arr.append(5)
print(arr.length())
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
