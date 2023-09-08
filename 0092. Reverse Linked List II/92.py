# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def helper(root, count, right):
            if count == right or not root or not root.next:
                return root, root

            newHead, newTail = helper(root.next, count + 1, right)
            root.next = newTail.next
            newTail.next = root
            return newHead, root

        tmpHead = ListNode(0, head)
        last = tmpHead
        count = 1
        while head:
            if count == left:
                newHead, newTail = helper(head, count, right)
                last.next = newHead
                break
            else:
                last = head
                head = head.next
                count += 1

        return tmpHead.next

    # Online solution
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmpHead = ListNode(0, head)
        prev = tmpHead
        cur = head

        i = 1
        for i in range(1, left):
            prev = cur
            cur = cur.next

        for i in range(right - left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

        return tmpHead.next

    # Based on online solution
    def reverseBetween3(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def helper(head):
            if not head or not head.next:
                return head

            newHead = helper(head.next)
            head.next.next = head
            head.next = None
            return newHead

        tmpHead = ListNode(0, head)
        prev = tmpHead
        leftHead = head
        for i in range(1, left):
            leftHead = leftHead.next
            prev = prev.next

        cur = leftHead
        for i in range(right - left):
            cur = cur.next

        rightHead = cur.next
        cur.next = None

        prev.next = helper(leftHead)
        leftHead.next = rightHead

        return tmpHead.next