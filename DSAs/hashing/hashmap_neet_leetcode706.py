class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

    def __str__(self):
        out, cur = '', self
        while cur:
            out += str(cur.val) + ":" + str(cur.key) + "->"
            cur = cur.next
        return out[:-2]

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(10)]

    def hash(self, key):
        print(key % len(self.map))
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def __str__(self):
        return '[' + ','.join([str(ln) for ln in self.map]) + ']'

h = MyHashMap()

h.put(1,1)

print(h)
