def count_rounds(numbers: list[int]) -> int:
    results = 1

    numbers_pos = dict()

    for i in range(len(numbers)):
        numbers_pos[numbers[i]] = i

    next = 1

    while next <= len(numbers):
        if next + 1 <= len(numbers) and numbers_pos[next] > numbers_pos[next + 1]: 
            results += 1

        next += 1

    return results

print(count_rounds([1, 2, 3, 4])) # 1
print(count_rounds([1, 3, 2, 4])) # 2
print(count_rounds([4, 3, 2, 1])) # 4
print(count_rounds([1])) # 1
print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

n = 10**5
numbers = list(reversed(range(1, n+1)))
print(count_rounds(numbers)) # 100000