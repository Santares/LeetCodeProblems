from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # slow
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        charDic = {}

        res = None
        current = res

        while head is not None:
            if head.val in charDic:
                charDic[head.val] += 1
            else:
                charDic[head.val] = 1
            head = head.next

        for k in charDic:
            if charDic[k] == 1:
                if current is None:
                    current = ListNode(k)
                    res = current
                    continue
                else:
                    current.next = ListNode(k)
                if res is None:
                    res = current
                current = current.next

        return res

    # slower
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next

        charDic = {}
        for c in temp:
            if c in charDic:
                charDic[c] += 1
            else:
                charDic[c] = 1

        temp.clear()
        for k in charDic:
            if charDic[k] == 1:
                temp.append(k)

        if len(temp) == 0:
            return None

        root = ListNode(temp[0])
        current = root
        for c in temp[1:]:
            current.next = ListNode(c)
            current = current.next

        return root

    # online solution
    def deleteDuplicates3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = ListNode(-float('inf'))
        remove = set()
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                remove.add(curr.val)
            else:
                prev = curr
            curr = curr.next
        curr = head
        prev = None
        while curr:
            if curr.val in remove:
                if curr == head:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
