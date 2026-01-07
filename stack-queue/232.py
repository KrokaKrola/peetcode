from collections import deque


class MyQueue:
    def __init__(self):
        self.stack = deque()
        self.helper = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # Transfer all elements to helper (reverses order)
        while len(self.stack) > 1:
            self.helper.append(self.stack.pop())

        # Get the bottom element (front of queue)
        result = self.stack.pop()

        # Transfer back to restore original order
        while self.helper:
            self.stack.append(self.helper.pop())

        return result

    def peek(self) -> int:
        # Transfer all elements to helper
        while len(self.stack) > 1:
            self.helper.append(self.stack.pop())

        # Peek at the bottom element
        result = self.stack[-1]

        # Transfer back to restore
        while self.helper:
            self.stack.append(self.helper.pop())

        return result

    def empty(self) -> bool:
        return len(self.stack) == 0
