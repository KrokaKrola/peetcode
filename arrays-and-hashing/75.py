class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for el in nums:
            counts[el] += 1

        k = 0
        for idx in range(len(counts)):
            for _ in range(counts[idx]):
                nums[k] = idx
                k += 1

    def sortColors_2(self, nums: list[int]) -> None:
        left, right = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1

            i += 1

    def sortColors_3(self, nums: list[int]) -> None:
        left, curr, right = 0, 0, len(nums) - 1

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while curr <= right:
            if nums[curr] < 1:
                swap(left, curr)
                left += 1
                curr += 1
            elif nums[curr] > 1:
                swap(curr, right)
                right -= 1
            else:
                curr += 1

        print(nums)


print(Solution().sortColors_3([2, 0, 2, 1, 1, 0]))
