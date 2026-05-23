class Solution:
    def check(self, nums: list[int]) -> bool:
        drops_count = 0

        for i in range(len(nums)):
            next_i = (i + 1) % len(nums)

            if nums[i] > nums[next_i]:
                drops_count += 1

        return drops_count < 2


print(Solution().check([3, 4, 5, 1, 2]))
print(Solution().check([2, 1, 3, 4]))
print(Solution().check([1, 2, 3]))
