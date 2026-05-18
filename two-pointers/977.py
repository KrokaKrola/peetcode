class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        results = [0] * len(nums)

        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                results[i] = nums[left] ** 2
                left += 1
            else:
                results[i] = nums[right] ** 2
                right -= 1

        return results


print(Solution().sortedSquares([-4, -1, 0, 1, 2, 3, 5]))
print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
print(Solution().sortedSquares([-5, -3, -2, -1]))
