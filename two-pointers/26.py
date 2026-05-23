class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lp, rp = 0, 1

        while rp < len(nums):
            if nums[lp] != nums[rp]:
                nums[lp + 1] = nums[rp]
                lp += 1
            rp += 1

        return lp + 1


print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(Solution().removeDuplicates([1, 1]))
print(Solution().removeDuplicates([1]))
