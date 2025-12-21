def twoSum(numbers: list[int], target: int) -> list[int]:
    lp = 0
    rp = len(numbers) - 1

    while lp < rp:
        res = numbers[lp] + numbers[rp]

        if res > target:
            rp -= 1
        elif res < target:
            lp += 1
        else:
            break

    return [lp + 1, rp + 1]


print(twoSum([2, 7, 11, 15], 9), [1, 2])
print(twoSum([2, 3, 4], 6), [1, 3])
print(twoSum([-1, 0], -1), [1, 2])
