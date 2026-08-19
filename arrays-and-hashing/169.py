class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elems = {}
        max_count = 0
        max_elem = nums[0]

        for num in nums:
            elems_count = elems.get(num, 0) + 1
            if elems_count > max_count:
                max_elem = num
                max_count = elems_count
            elems[num] = elems_count

        return max_elem

    def majorityElement2(self, nums: list[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


print(Solution().majorityElement2([3, 2, 3]))
print(Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement2([3, 3, 4]))
