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


print(sortedSquares([-4, -1, 0, 1, 2, 3, 5]))
