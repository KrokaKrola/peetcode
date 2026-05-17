def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum_val = numbers[left] + numbers[right]
        if sum_val > target:
            right -= 1
        elif sum_val < target:
            left += 1
        else:
            return [left + 1, right + 1]

    return []


print(twoSum([2, 7, 11, 15], 9), [1, 2])
print(twoSum([2, 3, 4], 6), [1, 3])
print(twoSum([-1, 0], -1), [1, 2])
