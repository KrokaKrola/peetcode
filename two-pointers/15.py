class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return results


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), "=", [[-1, -1, 2], [-1, 0, 1]])
print(Solution().threeSum([0, 1, 1]), "=", [])
print(Solution().threeSum([0, 0, 0]), "=", [0, 0, 0])
print(Solution().threeSum([0, 0, 0, 0]), "=", [0, 0, 0])
