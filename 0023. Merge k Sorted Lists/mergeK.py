from typing import Optional, List
from queue import PriorityQueue
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # too slow
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        root = ListNode()
        current = root

        def getMinNode(lastMin, lastIndex, newNode, newIndex):
            if lastMin is None:
                return newNode, newIndex
            if newNode.val < lastMin.val:
                return newNode, newIndex
            else:
                return lastMin, lastIndex

        while True:
            minNode = None
            minIndex = -1
            for i, node in enumerate(lists):
                if node is None:
                    continue
                else:
                    minNode, minIndex = getMinNode(minNode, minIndex, node, i)

            if minNode is None:
                break

            current.next = ListNode(minNode.val)
            current = current.next
            lists[minIndex] = lists[minIndex].next

        return root.next

    # cheat
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        root = ListNode()
        current = root

        temp = []
        for node in lists:
            while node:
                temp.append(node.val)
                node = node.next

        for x in sorted(temp):
            current.next = ListNode(x)
            current = current.next

        return root.next

    # slower
    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        root = ListNode()
        current = root

        q = PriorityQueue()
        for node in lists:
            while node:
                q.put((node.val))
                node = node.next

        while q.not_empty:
            x = q.get()
            current.next = ListNode(x)
            current = current.next

        return root.next

    # online solution
    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_list = []
        for lst in lists:
            node = lst
            while node is not None:
                node_list.append(node)
                node = node.next

        if node_list == []:
            return None

        node_list = sorted(node_list, key=lambda x: x.val)
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]

        node_list[-1].next = None

        return node_list[0]

    # online solution, fast
    def mergeKLists5(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tail = ListNode()

        min_heap = [(node.val, index) for index, node in enumerate(lists) if node]
        heapq.heapify(min_heap)

        while min_heap:
            _, list_index = heapq.heappop(min_heap)
            tail.next = lists[list_index]
            tail = tail.next
            node = lists[list_index] = lists[list_index].next

            if node:
                heapq.heappush(min_heap, (node.val, list_index))

        return head.next

    # online solution
    def mergeKLists6(self, lists):
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = ListNode(None)
        curr = dummy
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next


    def mergeKLists7(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        current = root

        count = 0
        queue = []
        for node in lists:
            while node:
                queue.append((node.val, count, node))
                count += 1
                node = node.next

        heapq.heapify(queue)
        while queue:
            _, _, node = heapq.heappop(queue)
            current.next = node
            current = current.next

        return root.next