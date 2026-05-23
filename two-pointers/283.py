class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lp, rp = 0, 0

        while rp < len(nums):
            if nums[rp] != 0:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
            rp += 1


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
print(Solution().moveZeroes([0]))
print(Solution().moveZeroes([1, 0, 1]))
print(Solution().moveZeroes([2, 1]))
