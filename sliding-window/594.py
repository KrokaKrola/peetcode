class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()

        left = 0
        max_len = 0

        for right in range(1, len(nums)):
            while nums[left] < nums[right] and nums[right] - nums[left] > 1:
                left += 1

            if nums[right] - nums[left] == 1:
                max_len = max(max_len, right - left + 1)

        return max_len


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(Solution().findLHS([1, 2, 3, 4]))
print(Solution().findLHS([1, 1, 1, 1]))
print(Solution().findLHS([1, 2, 2, 1]))
