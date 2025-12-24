def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    if min_length == float("inf"):
        return 0

    return min_length


def minSubArrayLen2(target: int, nums: list[int]) -> int:
    left = 0
    min_len = float("inf")
    curr_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0


print(minSubArrayLen2(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen2(4, [1, 4, 4]))
print(minSubArrayLen2(5, [5]))
print(minSubArrayLen2(11, [1, 1, 1, 1, 1, 1, 1]))
print(minSubArrayLen2(11, [1, 2, 3, 4, 5]))
