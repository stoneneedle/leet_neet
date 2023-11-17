head = [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# curr = head
# prev = None


# 1. get next list node (at start, 2->3->4->5), assign to var next
# 2. assign curr's next list node to prev, thereby always adding the last value to curr.next
# 3. add curr(final node(s)) to prev first, and the first one added will be the last node (1)
# 4. "iterate" by assigning next to curr, thereby removing previous node

# while curr:
#     next = curr.next # 1
#     curr.next = prev # 2
#     prev = curr # 3
#     curr = next # 4


class Solution:
    def reverseList(self, head):
        i = 0
        rev_list = ListNode()

        while i < len(head):
            next = i + 1 if i < len(head)-1 else 0
            rev_list.val = head[i]
            rev_list.next = head[next]
            i += 1
        return rev_list

s = Solution()
print(s.reverseList(head).val)
