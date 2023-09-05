class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        current = head
        while current:
            copied = Node(current.val)
            copied.next = current.next
            current.next = copied
            current = copied.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        dummy = Node(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next
 