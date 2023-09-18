# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            last = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = last
                last = cur
                cur = nxt
            return last, head

        groups = []
        count = 0
        head = head
        cur = head

        while cur:
            count += 1
            nxt = cur.next
            if count == k:
                cur.next = None
                groups.append(head)
                head = nxt
                count = 0

            cur = nxt

        res = None
        last = None
        for groupHead in groups:
            newHead, newTail = reverse(groupHead)
            if not res:
                res = newHead
            else:
                last.next = newHead
            last = newTail

        last.next = head

        return res
