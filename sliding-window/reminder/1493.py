def longestSubarray(nums: list[int]) -> int:
    result = 0
    left = 0
    zeroes = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1

        while zeroes > 1:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        result = max(result, right - left)

    return result


print(longestSubarray([1, 1, 0, 1]), 3)
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
print(longestSubarray([1, 1, 1]), 2)
print(longestSubarray([1]), 0)
print(longestSubarray([0]), 0)
print(longestSubarray([0, 0, 0]), 0)
