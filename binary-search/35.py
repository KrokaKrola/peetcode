class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo = -1
        hi = len(nums)

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid

        return hi


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
