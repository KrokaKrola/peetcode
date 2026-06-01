class Solution:
    def findFirst(self, nums: list[int], target: int) -> int:
        lo = -1
        hi = len(nums)

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid

        if hi == len(nums) or nums[hi] != target:
            return -1

        return hi

    def findLast(self, nums: list[int], target: int) -> int:
        lo = -1
        hi = len(nums)

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid

        if lo == -1 or nums[lo] != target:
            return -1

        return lo

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]
