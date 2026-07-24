class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      map = {}

      for i, n in enumerate(nums):
        complement = target - n

        if complement in map:
          return [map[complement], i]

        map[n] = i

      return []

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))
