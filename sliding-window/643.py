def findMaxAverage(nums: list[int], k: int) -> float:
    max_sum = sum(nums[:k])
    curr_sum = max_sum

    for i in range(1, len(nums) - k + 1):
        new_elem = nums[i + k - 1]
        old_elem = nums[i - 1]
        curr_sum = curr_sum - old_elem + new_elem
        max_sum = max(curr_sum, max_sum)

    return max_sum / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4), "12.75")
print(findMaxAverage([0, 1, 1, 3, 3], 4), "1.25")
print(findMaxAverage([5], 1), "5.0")
print(findMaxAverage([-1], 1), "-1.0")
print(findMaxAverage([0, 1, 1, 3, 3], 4), "2.0")
