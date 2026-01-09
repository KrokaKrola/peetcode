class StockSpanner:
    def __init__(self):
        self.spans = []
        self.prices = []

    def next(self, price: int) -> int:
        span = 1

        while self.prices and self.prices[-1] <= price:
            span += self.spans[-1]
            self.spans.pop()
            self.prices.pop()

        self.spans.append(span)
        self.prices.append(price)

        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(28))
print(obj.next(14))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))
