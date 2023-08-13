# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        queue = []
        dummyHead = ListNode(0, head)
        current = dummyHead

        while current:
            queue.append(current)
            current = current.next
            if len(queue) > n + 1:
                queue.pop(0)

        queue[0].next = queue[1].next

        return dummyHead.next

    # Two pointers, save space
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)

        left = dummyHead
        right = dummyHead

        while n:
            right = right.next
            n -= 1

        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummyHead.next



