class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_len = 0
        curr_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
                max_len = max(max_len, curr_count)
            else:
                curr_count = 0

        return max_len


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(Solution().findMaxConsecutiveOnes([1]))
print(Solution().findMaxConsecutiveOnes([0]))
