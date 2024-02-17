class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        new_head = dummy_head = head
        while head:
            size+=1
            head = head.next
        stop = size - n
        if stop == 0: return new_head.next
        counter = 1
        while dummy_head:
            if counter == stop:
                dummy_head.next = dummy_head.next.next
                return new_head
            counter+=1
            dummy_head = dummy_head.next