class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
      res = [0] * len(nums) * 2

      for i in range(len(nums)):
        res[i] = nums[i]
        res[len(nums) + i] = nums[i]

      return res

print(Solution().getConcatenation([1,2,1]))
