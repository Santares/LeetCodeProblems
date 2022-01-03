# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        while head:
            s += str(head.val)
            head = head.next

        return int(s, 2)

    # faster
    def getDecimalValue2(self, head: ListNode) -> int:
        res = 0
        while head:
            res *= 2
            res += head.val
            head = head.next

        return res