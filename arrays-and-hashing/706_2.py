class Slot:
    def __init__(self, key, value, state) -> None:
        self.key = key
        self.value = value
        self.state = state


class MyHashMap:
    """
    Hash Map implementation using Open Addressing (Linear Probing).

    Instead of storing collisions in linked lists, we probe for the next
    available slot in the array when a collision occurs.
    """

    EMPTY = -1
    TOMBSTONE = -2
    OCCUPIED = -3
    RESIZE_TRIGGER = 0.8

    def __init__(self):
        self.capacity = 64
        self.size = 0
        self.slots = [Slot(0, 0, self.EMPTY) for _ in range(self.capacity)]

    def resize(self):
        old_slots = self.slots
        self.capacity = self.capacity * 2
        self.size = 0
        self.slots = [Slot(0, 0, self.EMPTY) for _ in range(self.capacity)]

        for old_slot in old_slots:
            if old_slot.state == self.OCCUPIED:
                self.put(old_slot.key, old_slot.value)

    def put(self, key: int, value: int) -> None:
        if self.size / self.capacity >= self.RESIZE_TRIGGER:
            self.resize()

        idx = hash(key) % self.capacity
        first_tombstone_idx = -1

        while True:
            if self.slots[idx].state == self.EMPTY:
                if first_tombstone_idx != -1:
                    self.slots[first_tombstone_idx] = Slot(key, value, self.OCCUPIED)
                else:
                    self.size += 1
                    self.slots[idx] = Slot(key, value, self.OCCUPIED)
                return

            if self.slots[idx].state == self.TOMBSTONE and first_tombstone_idx == -1:
                first_tombstone_idx = idx

            if self.slots[idx].state == self.OCCUPIED and self.slots[idx].key == key:
                self.slots[idx].value = value
                return

            idx = (idx + 1) % self.capacity

    def get(self, key: int) -> int:
        idx = hash(key) % self.capacity

        while True:
            if self.slots[idx].state == self.EMPTY:
                return -1
            elif self.slots[idx].state == self.OCCUPIED and self.slots[idx].key == key:
                return self.slots[idx].value

            idx = (idx + 1) % self.capacity

    def remove(self, key: int) -> None:
        idx = hash(key) % self.capacity

        while True:
            if self.slots[idx].state == self.OCCUPIED and self.slots[idx].key == key:
                self.slots[idx].state = self.TOMBSTONE
                return
            elif self.slots[idx].state == self.EMPTY:
                return

            idx = (idx + 1) % self.capacity


# Test: basic LeetCode 706 example
print("--- basic ---")
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))  # 1
print(obj.get(3))  # -1
obj.put(2, 1)
print(obj.get(2))  # 1
obj.remove(2)
print(obj.get(2))  # -1

# Test: overwrite existing key
print("--- overwrite ---")
obj = MyHashMap()
obj.put(5, 10)
print(obj.get(5))  # 10
obj.put(5, 99)
print(obj.get(5))  # 99

# Test: remove key that doesn't exist (should be no-op)
print("--- remove missing key ---")
obj = MyHashMap()
obj.remove(42)
print(obj.get(42))  # -1

# Test: reinsert after remove reuses tombstone
print("--- reinsert after remove ---")
obj = MyHashMap()
obj.put(7, 1)
obj.remove(7)
print(obj.get(7))  # -1
obj.put(7, 2)
print(obj.get(7))  # 2

# Test: search doesn't stop early at a tombstone (probe chain integrity)
print("--- probe chain survives tombstone ---")
obj = MyHashMap()
# Force collisions by reusing the same low-order bits: pick keys that
# collide mod capacity (capacity starts at 64).
k1, k2, k3 = 1, 65, 129  # all hash to the same slot (1 % 64 == 65 % 64 == 129 % 64)
obj.put(k1, 1)
obj.put(k2, 2)
obj.put(k3, 3)
obj.remove(k2)  # tombstone in the middle of the probe chain
print(obj.get(k1))  # 1
print(obj.get(k3))  # 2 (must still be found past the tombstone)
print(obj.get(k2))  # -1

# Test: resize triggers and existing keys remain retrievable
print("--- resize preserves entries ---")
obj = MyHashMap()
n = 100
for i in range(n):
    obj.put(i, i * 10)
print(obj.capacity >= n)  # True, should have grown
print(all(obj.get(i) == i * 10 for i in range(n)))  # True

# Test: many put/remove cycles on the same key (tombstone churn)
print("--- churn on same key ---")
obj = MyHashMap()
for i in range(50):
    obj.put(1, i)
    obj.remove(1)
obj.put(1, 999)
print(obj.get(1))  # 999
