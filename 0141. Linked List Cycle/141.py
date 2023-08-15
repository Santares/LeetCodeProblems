# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            if head in visited:
                return True
            visited[head] = 1
            head = head.next

        return False

    # A little improved
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        left, right = head, head
        while True:
            if not right or not right.next:
                return False
            right = right.next.next
            left = left.next
            if left == right:
                return True