def minSubArrayLen(target: int, nums: list[int]) -> int:
    result = float("inf")
    left = 0

    sum = 0

    for right in range(len(nums)):
        sum += nums[right]

        while sum >= target:
            result = min(result, right - left + 1)
            sum -= nums[left]
            left += 1

    return result if result != float("inf") else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
print(minSubArrayLen(4, [1, 4, 4]), 1)
print(minSubArrayLen(5, [5]), 1)
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1]), 0)
print(minSubArrayLen(11, [1, 2, 3, 4, 5]), 3)
