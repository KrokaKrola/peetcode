class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
      prev_numbers: set[int] = set()

      for el in nums:
        if el in prev_numbers:
          return True

        prev_numbers.add(el)

      return False

print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
