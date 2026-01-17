from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        map = defaultdict(int)

        for el in nums:
            map[el] += 1

        max_el = None
        max_val = 0

        for el in map:
            if map[el] > max_val:
                max_el = el
                max_val = map[el]

        return max_el

    def majorityElement2(self, nums: list[int]) -> int:
        count = 0
        candidate = 0

        for el in nums:
            if count == 0:
                candidate = el
                count += 1
            elif el == candidate:
                count += 1
            else:
                count -= 1

        return candidate


print(Solution().majorityElement2([3, 2, 3]))
print(Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2]))
