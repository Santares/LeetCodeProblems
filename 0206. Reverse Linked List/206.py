# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        last = head
        current = head.next
        head.next = None
        while current:
            new = current.next
            current.next = last
            last = current
            current = new

        return last

    # Improved version of solution1
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        current = head
        while current:
            new = current.next
            current.next = last
            last = current
            current = new

        return last
