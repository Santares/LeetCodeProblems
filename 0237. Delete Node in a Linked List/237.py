# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        cur = node
        while True:
            cur.val = cur.next.val
            if cur.next.next is None:
                cur.next = None
                break
            cur = cur.next



class Solution2:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next