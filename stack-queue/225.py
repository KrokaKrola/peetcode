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
        target = self.pop()
        self.queue.append(target)
        return target

    def empty(self) -> bool:
        return len(self.queue) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())
