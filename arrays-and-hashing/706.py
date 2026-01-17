class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class LinkedList:
    head: Node = None

    def __init__(self):
        print()

    def get(self, key: int) -> int:
        current = self.head

        while current:
            if current.key == key:
                return current.val

            current = current.next

        return -1

    def put(self, key: int, val: int) -> None:
        current = self.head

        while current:
            if current.key == key:
                current.val = val
                return

            current = current.next

        self.head = Node(key, val, self.head)

    def remove(self, key: int) -> None:
        if not self.head:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head

        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


class MyHashMap:
    n: int
    buckets: list[LinkedList]

    def __init__(self):
        self.n = 991
        self.buckets = [LinkedList() for _ in range(self.n)]

    def hash(self, x: int) -> int:
        return x % self.n

    def put(self, key: int, value: int) -> None:
        n = self.hash(key)
        self.buckets[n].put(key, value)

    def get(self, key: int) -> int:
        n = self.hash(key)
        return self.buckets[n].get(key)

    def remove(self, key: int) -> None:
        n = self.hash(key)
        self.buckets[n].remove(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 2)
param_2 = obj.get(1)
obj.remove(1)
print(obj)
