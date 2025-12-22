def findMaxAverage(nums: list[int], k: int) -> float:
    max_sum = sum(nums[:k])
    curr_sum = max_sum

    for i in range(k, len(nums)):
        curr_sum -= nums[i - k]
        curr_sum += nums[i]

        max_sum = max(curr_sum, max_sum)

    return max_sum / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([0, 1, 1, 3, 3], 4))
print(findMaxAverage([5], 1))
print(findMaxAverage([-1], 1))
