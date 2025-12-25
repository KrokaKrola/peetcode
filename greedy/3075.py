def maximumHappinessSum(happiness: list[int], k: int) -> int:
    sum = 0
    happiness = sorted(happiness, reverse=True)

    for i in range(k):
        sum += happiness[i] - i if happiness[i] - i >= 0 else 0

    return sum


# print(maximumHappinessSum([1, 2, 3], 2), 4)
print(maximumHappinessSum([12, 1, 42], 3), 53)
