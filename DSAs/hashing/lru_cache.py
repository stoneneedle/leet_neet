import json

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

    def __str__(self):
        return 'Node(' + str(self.key) + ', ' + str(self.val) + ')'

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from list and delete LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def __str__(self):
        out = 'LRUCache: ({'
        for key, val in self.cache.items():
            out += str(key) + ': ' + str(key) + ", "
        return out + "capacity: " + str(self.cap) + ')}'

lc = LRUCache(2)

lc.put(1, 1)
lc.put(2, 2)
lc.put(3, 3)
lc.put(4, 4)

print(lc)