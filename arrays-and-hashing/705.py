# class MyHashSet:
#     def __init__(self):
#         self.data = []

#     def add(self, key: int) -> None:
#         if key not in self.data:
#             self.data.append(key)

#     def remove(self, key: int) -> None:
#         if key in self.data:
#             self.data.remove(key)

#     def contains(self, key: int) -> bool:
#         return key in self.data


class ListNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)  # pyright: ignore[reportAttributeAccessIssue]

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))
