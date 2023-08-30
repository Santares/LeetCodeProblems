class Node:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cap = capacity
        self.size = 0
        self.map = {}

    def move(self, node: Node) -> None:
        if self.head != node:
            node.prev.next = node.next
            if self.tail == node:
                self.tail = node.prev
            else:
                node.next.prev = node.prev
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

    def get(self, key: int) -> int:
        if key in self.map and self.map[key] is not None:
            node = self.map[key]
            self.move(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map and self.map[key] is not None:
            node = self.map[key]
            node.value = value
            self.move(node)
        else:
            newNode = Node(key, value, None, self.head)
            self.map[key] = newNode
            if not self.head:
                self.head = newNode
                self.tail = newNode
            else:
                self.head.prev = newNode
                self.head = newNode

            self.size += 1
            if self.size > self.cap:
                self.map[self.tail.key] = None
                self.tail = self.tail.prev
                self.tail.next = None
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    capacity = 2
    capacity = 3
    obj = LRUCache(capacity)

    # obj.put(1,1)
    # obj.put(2, 2)
    # param_1 = obj.get(1)
    # obj.put(3, 3)
    # param_1 = obj.get(2)
    # obj.put(4, 4)
    # param_1 = obj.get(1)
    # param_1 = obj.get(3)
    # param_1 = obj.get(4)

    obj.put(1, 1)
    obj.put(2, 2)
    obj.put(3, 3)
    obj.put(4, 4)
    param_1 = obj.get(4)
    param_1 = obj.get(3)
    param_1 = obj.get(2)
    param_1 = obj.get(1)


    print("End")


