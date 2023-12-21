from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow
        last = None
        while cur:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp

        l = head
        r = last
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
