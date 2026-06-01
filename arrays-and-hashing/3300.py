class Solution:
    def minElement(self, nums: list[int]):
        result = float("inf")

        for el in nums:
            tmp = 0

            while el > 0:
                tmp += el % 10
                el = el // 10

            result = min(result, tmp)

        return result


print(Solution().minElement([10, 12, 13, 14]), 1)
print(Solution().minElement([1, 2, 3, 4]), 1)
print(Solution().minElement([999, 19, 199]), 10)
