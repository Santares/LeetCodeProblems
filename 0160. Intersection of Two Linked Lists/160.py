# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = {}
        while headA:
            visited[headA] = 1
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            else:
                headB = headB.next

        return None

    # Two pointers, fast and save space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        iA = headA
        iB = headB

        while iA != iB:
            iA = iA.next if iA != None else headB
            iB = iB.next if iB != None else headA

        return iA
