def count_numbers(a: int, b: int) -> int:
    nums = [2, 5]

    for n in nums:
        if n <= b:
            nums.append(n * 10 + 2)
            nums.append(n * 10 + 5)

    results = 0

    for n in nums:
        if a <= n <= b:
            results += 1

    return results


print(count_numbers(1, 100))  # 6
print(count_numbers(60, 70))  # 0
print(count_numbers(25, 25))  # 1
print(count_numbers(1, 10**9))  # 1022
print(count_numbers(123456789, 987654321))  # 512
print(count_numbers(1, 3))  # 1
