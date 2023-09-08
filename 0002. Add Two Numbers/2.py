# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 2023/09/08
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        tmpHead = ListNode(0)
        cur = tmpHead
        while l1 and l2:
            total = l1.val + l2.val + flag
            val = total % 10
            flag = total // 10
            cur.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        nxt = None
        if l1:
            nxt = l1
        else:
            nxt = l2

        while nxt:
            total = nxt.val + flag
            val = total % 10
            flag = total // 10
            cur.next = ListNode(val)
            nxt = nxt.next
            cur = cur.next

        if flag:
            cur.next = ListNode(1)

        return tmpHead.next
