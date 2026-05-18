def find_rounds(numbers: list[int]) -> list[list[int]]:
    results: list[list[int]] = []

    positions = dict()

    for i in range(len(numbers)):
        positions[numbers[i]] = i

    next = 1
    round = [next]

    while next != len(numbers):
        if positions[next] < positions[next + 1]:
            round.append(next + 1)
            next += 1
        else:
            results.append(round)
            next += 1
            round = [next]

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
