class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}

    def delete(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node: Node) -> None:
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        node = self.data[key]
        self.delete(node)
        self.addToHead(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.value = value
            self.delete(node)
            self.addToHead(node)
            return

        if len(self.data) >= self.capacity:
            node = self.tail.prev
            self.delete(node)
            del self.data[node.key]

        node = Node(key, value)
        self.addToHead(node)
        self.data[key] = node


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
