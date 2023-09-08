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

    # Online solution
    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newHead = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return newHead

    # Based on online solution
    def reverseList4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmpHead = ListNode(0, head)
        prev = tmpHead
        cur = head

        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

        return tmpHead.next

if __name__ == '__main__':
    s = Solution()
    test = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(s.reverseList3(test))