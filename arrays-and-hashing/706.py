class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.data = [Node(0, 0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        idx = key % 10**4
        cur = self.data[idx]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return

            cur = cur.next

        cur.next = Node(key, value)  # pyright: ignore[reportAttributeAccessIssue]

    def get(self, key: int) -> int:
        idx = key % 10**4
        cur = self.data[idx]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value

            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        idx = key % 10**4
        cur = self.data[idx]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 2)
param_2 = obj.get(1)
print(param_2)
obj.remove(1)
