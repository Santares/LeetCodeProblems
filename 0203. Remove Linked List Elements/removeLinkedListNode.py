from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            node = cur
            while node.next and node.next.val == val:
                node = node.next
            cur.next = node.next
            cur = cur.next

        return dummy.next

    # faster
    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last = dummy

        while head:
            if head.val != val:
                last.next = head
                last = last.next
            head = head.next

        last.next = None

        return dummy.next