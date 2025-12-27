def maxProfit(prices: list[int]) -> int:
    result = 0
    left = 0

    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            left = right
            continue

        result = max(result, prices[right] - prices[left])

    return result


print(maxProfit([7, 1, 5, 3, 6, 4]), 5)
print(maxProfit([7, 6, 5, 4, 3, 1]), 0)
print(maxProfit([1]), 0)
print(maxProfit([2, 1, 2, 1, 0, 1, 2]), 2)
print(maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]), 9)
