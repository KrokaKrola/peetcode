from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while t - self.queue[0] > 3000:
            self.queue.popleft()

        return len(self.queue)


rc = RecentCounter()
print(rc.ping(642))
print(rc.ping(1849))
print(rc.ping(4921))
print(rc.ping(5936))
print(rc.ping(5957))
