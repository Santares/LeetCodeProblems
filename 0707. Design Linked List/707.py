class MyLinkedList:
    myList = []

    def __init__(self):
        self.myList = []

    def get(self, index: int) -> int:
        if index < len(self.myList):
            return self.myList[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.myList = [val] + self.myList

    def addAtTail(self, val: int) -> None:
        self.myList.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.myList):
            self.myList = self.myList[:index] + [val] + self.myList[index:]

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.myList):
            self.myList = self.myList[:index] + self.myList[index + 1:]


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Linked list
class MyLinkedList2:

    def __init__(self):
        self.dummyHead = ListNode(-1, None)

    def get(self, index: int) -> int:
        current = self.dummyHead.next
        while index > 0 and current != None:
            index -= 1
            current = current.next
        if index == 0 and current != None:
            return current.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.dummyHead.next = ListNode(val, self.dummyHead.next)

    def addAtTail(self, val: int) -> None:
        current = self.dummyHead
        while current.next:
            current = current.next
        current.next = ListNode(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.dummyHead
        while index > 0 and current.next != None:
            index -= 1
            current = current.next
        if index == 0 and current != None:
            current.next = ListNode(val, current.next)

    def deleteAtIndex(self, index: int) -> None:
        current = self.dummyHead
        while index > 0 and current.next != None:
            index -= 1
            current = current.next
        if index == 0 and current.next != None:
            current.next = current.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)