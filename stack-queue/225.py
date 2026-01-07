from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        tmp = deque()
        for _ in range(len(self.queue) - 1):
            tmp.append(self.queue.popleft())

        target = self.queue.popleft()
        self.queue = tmp
        return target

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStack2:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


myStack = MyStack2()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())
