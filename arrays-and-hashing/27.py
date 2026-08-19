class Solution:
    # two pointers approach
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        l = 0

        while l < n:
            if nums[l] == val:
                n -= 1
                nums[l] = nums[n]
            else:
                l += 1

        return n

    def removeElement2(self, nums: list[int], val: int) -> int:
        write_pos = 0

        for num in nums:
            if num != val:
                nums[write_pos] = num
                write_pos += 1

        return write_pos


print(Solution().removeElement([3, 2, 2, 3], 3), 2)
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
