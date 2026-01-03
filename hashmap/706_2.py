class MyHashMap:
    """
    Hash Map implementation using Open Addressing (Linear Probing).

    Instead of storing collisions in linked lists, we probe for the next
    available slot in the array when a collision occurs.
    """

    def __init__(self):
        self.size = 2069  # Prime number for better distribution
        self.keys = [None] * self.size
        self.values = [None] * self.size
        # We use a special marker for deleted slots
        self.DELETED = object()

    def _hash(self, key: int) -> int:
        return key % self.size

    def _probe(self, key: int) -> int:
        """
        Find the index where key is or should be stored.
        Uses linear probing: if slot is taken, check next slot.
        """
        index = self._hash(key)
        first_deleted = -1  # Track first deleted slot for insertion optimization

        while self.keys[index] is not None:
            # Found the key
            if self.keys[index] == key:
                return index

            # Track first deleted slot we encounter
            if self.keys[index] is self.DELETED and first_deleted == -1:
                first_deleted = index

            # Linear probing: move to next slot
            index = (index + 1) % self.size

        # Key not found - return first deleted slot if available, else empty slot
        return first_deleted if first_deleted != -1 else index

    def put(self, key: int, value: int) -> None:
        index = self._probe(key)
        self.keys[index] = key
        self.values[index] = value

    def get(self, key: int) -> int:
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Mark as deleted (can't just set to None - would break probing)
                self.keys[index] = self.DELETED
                self.values[index] = None
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
