class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        result = [-1] * len(nums)
        left = 0
        curr_summ = 0

        window_size = k * 2 + 1

        for right in range(len(nums)):
            curr_summ += nums[right]
            curr_window_size = right - left + 1

            if curr_window_size >= window_size:
                result[right - k] = curr_summ // window_size
                curr_summ -= nums[left]
                left += 1

        return result


print(Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
print(Solution().getAverages([100000], 0))
print(Solution().getAverages([8], 10000))
