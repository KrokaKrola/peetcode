class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            pivot = (lp + rp) // 2

            if nums[pivot] == target:
                return pivot

            if nums[pivot] > target:
                rp = pivot - 1
            elif nums[pivot] < target:
                lp = pivot + 1

        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
print(Solution().search([5], 5))
