class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_of_min_values = []

    def push(self, val: int) -> None:
        if not self.stack_of_min_values:
            self.stack_of_min_values.append((val, 1))
        else:
            old_min, old_min_count = self.stack_of_min_values[-1]
            new_min = min(old_min, val)
            if new_min == old_min:
                self.stack_of_min_values[-1] = (old_min, old_min_count + 1)
            else:
                self.stack_of_min_values.append((new_min, 1))

        self.stack.append(val)

    def pop(self) -> None:
        min_value, min_value_count = self.stack_of_min_values[-1]
        if min_value_count == 1:
            self.stack_of_min_values.pop()
        else:
            self.stack_of_min_values[-1] = (min_value, min_value_count - 1)
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_value, _ = self.stack_of_min_values[-1]
        return min_value


ms = MinStack()
ms.push(2)
ms.push(0)
ms.push(3)
ms.push(0)
print(ms.getMin())
ms.pop()
print(ms.getMin())
ms.pop()
print(ms.getMin())
ms.pop()
print(ms.getMin())
ms.pop()
