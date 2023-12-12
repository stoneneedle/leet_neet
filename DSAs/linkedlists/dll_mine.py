class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        out, cur = '', self
        while cur:
            out += str(cur.val) + "<->"
            cur = cur.next
        return out[:-3]


# Implementation for Doubly Linked List
class DoublyLinkedList:
    def __init__(self, _list=[]):
        # Init the list with 'dummy' head and tail nodes which makes
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        for elem in _list:
            self.insert_end(elem)

    def insert_front(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insert_end(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def remove_front(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def remove_end(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def __str__(self):
        return str(self.head.next)[:-5]


dll = DoublyLinkedList([1,2,3,4,5,6,7])
dll.remove_end()
dll.remove_front()
print(dll)
