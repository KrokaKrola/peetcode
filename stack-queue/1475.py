class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        result = prices.copy()

        for idx in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[idx]:
                result[stack[-1]] = prices[stack[-1]] - prices[idx]
                stack.pop()

            stack.append(idx)

        return result


print(Solution().finalPrices([8, 4, 6, 2, 3]))
print(Solution().finalPrices([1, 2, 3, 4, 5]))
print(Solution().finalPrices([10, 1, 1, 6]))
