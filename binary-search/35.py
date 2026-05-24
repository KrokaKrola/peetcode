class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            pivot = (lp + rp) // 2
            if nums[pivot] == target:
                return pivot

            if nums[pivot] > target:
                rp = pivot - 1
            elif nums[pivot] < target:
                lp = pivot + 1

        return lp


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
