class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity

    # Insert n into arr at the next open position.
    # Length is the number of 'real' values in arr, and capacity
    # is the size (aka memory allocated for the fixed size array).
    def insertEnd(self, n, length):
        if length < self.capacity:
            self.arr[length] = n

    # Remove from the last position in the array if the array
    # is not empty (i.e. length is non-zero).
    def removeEnd(self, length):
        if length > 0:
            # Overwrite last element with some default value.
            # We would also consider the length to be decreased by 1.
            self.arr[length - 1] = 0

    # Insert n into index i after shifting elements to the right.
    # Assuming i is a valid index and arr is not full.
    def insertMiddle(self, i, n, length):
        # Shift starting from the end to i.
        for index in range(length - 1, i - 1, -1):
            self.arr[index + 1] = self.arr[index]

        # Insert at i
        self.arr[i] = n

    # Remove value at index i before shifting elements to the left.
    # Assuming i is a valid index.
    def removeMiddle(self, i, length):
        # Shift starting from i + 1 to end.
        for index in range(i + 1, length):
            self.arr[index - 1] = self.arr[index]
        # No need to 'remove' arr[i], since we already shifted

    def __str__(self):
        out = ''
        for i in range(self.capacity):
            out += str(self.arr[i]) + ", "
        return "[" + str(out) + "]"

sa = StaticArray(10)

sa.insertEnd(3, 0)
sa.insertEnd(10, 1)
sa.insertEnd(23, 2)
sa.removeMiddle(1, 3)

print(sa)

