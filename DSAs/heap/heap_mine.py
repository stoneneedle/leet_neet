class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2],self.heap[i]
            i = i // 2

    def __str__(self):
        return str(self.heap)

h = Heap()
h.heap = [0,14,19,16,21,26,19,68,65,30,None,None,None,None,None,None]
h.push(2)

print(h)

# Note: 0th value is ignored, and not part of the heap

# for any value, say 19 (index 2), the parent is i/2 (index 1, value 14),
# the left child is 2*i (index 4, value 21), and the right child is 2*i+1 (index 5, value 26)
