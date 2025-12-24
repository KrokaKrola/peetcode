def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    zeroes_count = 0
    max_number = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes_count += 1

        while zeroes_count > k:
            if nums[left] == 0:
                zeroes_count -= 1

            left += 1

        max_number = max(max_number, right - left + 1)

    return max_number


print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), "6")
print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), "10")
print(longestOnes([0, 0, 0, 1], 4), "4")
print(longestOnes([1, 1, 1, 1], 2), "4")
print(longestOnes([0], 0), "0")
print(longestOnes([1, 0, 1, 1], 0), "2")
