class MyHashMap:
    """
    Hash Map implementation using Open Addressing (Linear Probing).

    Instead of storing collisions in linked lists, we probe for the next
    available slot in the array when a collision occurs.
    """

    EMPTY = -1
    DELETED = -2

    def __init__(self):
        # Larger prime to keep load factor low (10^4 operations max)
        self.size = 10007
        self.keys = [self.EMPTY] * self.size
        self.values = [0] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        first_deleted = -1

        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                self.values[index] = value
                return
            if self.keys[index] == self.DELETED and first_deleted == -1:
                first_deleted = index
            index = (index + 1) % self.size

        # Use first deleted slot if found, otherwise use empty slot
        if first_deleted != -1:
            index = first_deleted
        self.keys[index] = key
        self.values[index] = value

    def get(self, key: int) -> int:
        index = self._hash(key)

        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)

        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                self.keys[index] = self.DELETED
                return
            index = (index + 1) % self.size


# Test
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))  # 1
print(obj.get(3))  # -1
obj.put(2, 1)
print(obj.get(2))  # 1
obj.remove(2)
print(obj.get(2))  # -1
