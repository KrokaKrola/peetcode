def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    result = []

    for targetIdx in range(len(nums)):
        if targetIdx > 0 and nums[targetIdx] == nums[targetIdx - 1]:
            continue

        target = -nums[targetIdx]
        left = targetIdx + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                result.append([nums[targetIdx], nums[left], nums[right]])
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0]))
print(threeSum([0, 0, 0, 0]))
print(threeSum([-1, 0, 1, 0]))
