class Array:
  def __init__(self, array=None):
    if array is None:
      array = []
    if not isinstance(array, list):
      raise TypeError("The input should be a list.")
    self.array = array

  def length(self):
    """Returns the current size/number of elements of the array."""
    count = 0
    for _ in self.array:
      count += 1
    return count

  def append(self, value):
    """Adds a new element to the array"""
    self.array += [value]

  def insert(self, index, value):
    """Adds a new element at a specific position in the array."""
    if not isinstance(index, int):
      raise TypeError("Index should be an integer.")
    if index < 0 or index > self.length():
      raise IndexError("Index out of bounds")

    # shift elements to make room for the new value
    self.array += [None]  
    for i in range(self.length() - 1, index, -1):
      self.array[i] = self.array[i - 1]
    self.array[index] = value

  def remove(self, value):
    """Removes the first occurrence of the specified value from the array."""
    found = False
    for i in range(self.length()):
      if self.array[i] == value:
        found = True
        for j in range(i, self.length() - 1):
          self.array[j] = self.array[j + 1]
        self.array = self.array[:-1]
        break
    if not found:
      raise ValueError(f"{value} not found in the array.")

  def contains(self, value):
    """Checks if the value exists in the array."""
    for item in self.array:
      if item == value:
        return True
    return False

  def clear(self):
    """Reset the array to an empty list"""
    self.array = []

  def is_equal(self, other):
    """Compares if two arrays are equal."""
    if not isinstance(other, (Array, list)):
      raise TypeError("The comparison must be with an Array or a list.")
    if self.length() != (other.length() if isinstance(other, Array) else len(other)):
      return False

    for i in range(self.length()):
      if self.array[i] != other.array[i]:
        return False
    return True

  def pop(self, index=None):
    """Removes and returns an element from a specific position."""
    if self.length() == 0:
      raise IndexError("Cannot pop from an empty array")

    if index is None:
      # If no index is provided, remove the last element
      index = self.length() - 1

    if index < 0 or index >= self.length():
      raise IndexError("Index out of bounds")

    # Pop the element at the specified index
    value = self.array[index]
    for i in range(index, self.length() - 1):
      self.array[i] = self.array[i + 1]
    self.array = self.array[:-1]
    return value

  def concatenate(self, other):
    """Concatenates the current array with another array or list."""
    # Ensure that 'other' is an iterable (list or array)
    if isinstance(other, Array):
      other = other.array

    # add elements of 'other' to the current array
    for item in other:
      self.array.append(item)

  def delete(self, index):
    """Deletes the element at a specific index."""
    if not isinstance(index, int):
      raise TypeError("Index must be an integer.")

    if index < 0 or index >= self.length():
      raise IndexError("Index out of bounds")

    for i in range(index, self.length() - 1):
      self.array[i] = self.array[i + 1]
    self.array = self.array[:-1]

  def __repr__(self):
    """String representation of the array."""
    return f"Array({self.array})"
