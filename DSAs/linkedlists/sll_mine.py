class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        out, cur = '', self
        while cur:
            out += str(cur.val) + "->"
            cur = cur.next
        return out[:-2]

class SinglyLinkedList:
    def __init__(self, from_list=[]):
        # Dummy node
        self.head = ListNode(-1)
        self.tail = self.head

        for elem in from_list:
            self.insert_tail(elem)

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds

    def insert_head(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:  # if list was empty before inserting
            self.tail = new_node

    def insert_tail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            # move curr to node before target node
            i += 1
            curr = curr.next

        if index == 0:
            self.head.next = self.head.next.next
        elif index > 0 and curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def __str__(self):
        return str(self.head.next)

sll = SinglyLinkedList([1,2,3,5,6,7])
# sll.insert_tail(1)
# sll.insert_tail(2)
# sll.insert_tail(3)
print(sll)
