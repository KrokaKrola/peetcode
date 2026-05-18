def find_rounds(numbers: list[int]) -> list[list[int]]:
    results: list[list[int]] = []

    numbers_pos = dict()

    for i in range(len(numbers)):
        numbers_pos[numbers[i]] = i

    next = 1
    round: list[int] = []

    while next <= len(numbers):
        round.append(next)

        if next + 1 <= len(numbers) and numbers_pos[next] > numbers_pos[next + 1]: 
            results.append(round)
            round = []

        next += 1

    if len(round) > 0:
        results.append(round)

    return results


print(find_rounds([1, 2, 3, 4]))
# [[1, 2, 3, 4]]

print(find_rounds([1, 3, 2, 4]))
# [[1, 2], [3, 4]]

print(find_rounds([4, 3, 2, 1]))
# [[1], [2], [3], [4]]

print(find_rounds([1]))
# [[1]]

print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
# [[1], [2, 3], [4, 5, 6], [7, 8]]
