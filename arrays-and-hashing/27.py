class Solution:
    # two pointers approach
    def removeElement(self, nums: list[int], val: int) -> int:
        result = 0
        tp = 0
        bp = 0

        while bp < len(nums):
            if nums[bp] == val:
                while tp < len(nums) - 1 and nums[tp] == val:
                    tp += 1

                if nums[tp] == val:
                    bp += 1
                    continue

                tmp = nums[tp]
                nums[tp] = nums[bp]
                nums[bp] = tmp
            else:
                tp += 1

            bp += 1
            result += 1

        return result

    def removeElement2(self, nums: list[int], val: int) -> int:
        write_pos = 0

        for num in nums:
            if num != val:
                nums[write_pos] = num
                write_pos += 1

        return write_pos


print(Solution().removeElement2([3, 2, 2, 3], 3))
print(Solution().removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2))
