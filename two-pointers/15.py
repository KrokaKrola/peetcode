class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)):
            # skipping same element as before, for not first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -1 * nums[i]

            while left < right:
                tmp_sum = nums[left] + nums[right]
                if tmp_sum > target:
                    right -= 1
                elif tmp_sum < target:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1

                    # move forward for for consecutive elements with the same value as lts left value
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return results


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), "=", [[-1, -1, 2], [-1, 0, 1]])
# print(Solution().threeSum([0, 1, 1]), [])
# print(Solution().threeSum([0, 0, 0]), [0, 0, 0])
print(Solution().threeSum([0, 0, 0, 0]), [0, 0, 0])
