from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
            head = head.next

        return None

    # Based on online solution, two pointers, save space
    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while True:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow