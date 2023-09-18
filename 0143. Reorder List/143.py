# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        left = 0
        right = len(values) - 1

        cur = head
        count = 1
        while cur:
            if count % 2 == 1:
                cur.val = values[left]
                left += 1
            else:
                cur.val = values[right]
                right -= 1
            count += 1
            cur = cur.next

    # Based on online solution
    def reorderList2(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            last = None
            while head:
                nxt = head.next
                head.next = last
                last = head
                head = nxt
            return last

        def findMid(head):
            slow, fast = head, head
            while fast:
                fast = fast.next
                if fast:
                    fast = fast.next
                    slow = slow.next
            return slow

        def merge(first, second):
            while first and second:
                tmp1 = first.next
                tmp2 = second.next
                first.next = second
                second.next = tmp1
                second = tmp2
                first = tmp1

        mid = findMid(head)
        right = reverse(mid.next)
        mid.next = None
        left = head
        merge(left, right)
