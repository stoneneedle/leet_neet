### I just need a simple way to VISUALIZE this data structure and output it!

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        out, cur = '', self
        while cur:
            out += str(cur.val) + " -> "
            cur = cur.next
        return out[:-4]

ln = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))

print(len(ln))
