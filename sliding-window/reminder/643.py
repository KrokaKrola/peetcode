def findMaxAverage(nums: list[int], k: int) -> float:
    max_sum = -float("inf")
    left = 0

    curr_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        window_size = right - left + 1

        if window_size > k:
            at_most_left_el = nums[left]
            curr_sum -= at_most_left_el
            left += 1

        if window_size == k:
            max_sum = max(curr_sum, max_sum)

    return max_sum / k


# print(findMaxAverage([1, 12, -5, -6, 50, 3], 4), "12.75")
# print(findMaxAverage([0, 1, 1, 3, 3], 4), "2")
# print(findMaxAverage([5], 1), "5.0")
# print(findMaxAverage([-1], 1), "-1.0")
# print(findMaxAverage([0, 1, 1, 3, 3], 4), "2.0")
