def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    output = [0] * n

    lp = 0
    rp = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[lp]) < abs(nums[rp]):
            output[i] = nums[rp] * nums[rp]
            rp -= 1
        else:
            output[i] = nums[lp] * nums[lp]
            lp += 1

    return output


def sortedSquares2(nums: list[int]) -> list[int]:
    n = len(nums)
    results = [0] * n

    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            results[i] = nums[right] * nums[right]
            right -= 1
        else:
            results[i] = nums[left] * nums[left]
            left += 1

    return results


print(sortedSquares([-4, -1, 0, 1, 2, 3, 5]))
print(sortedSquares2([-4, -1, 0, 1, 2, 3, 5]))
