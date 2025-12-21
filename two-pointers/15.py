def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    result = []

    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lp = i + 1
        rp = n - 1

        while lp < rp:
            total = nums[i] + nums[lp] + nums[rp]
            if total > 0:
                rp -= 1
            elif total < 0:
                lp += 1
            else:
                result.append([nums[i], nums[lp], nums[rp]])
                lp += 1

                while nums[lp] == nums[lp - 1] and lp < rp:
                    lp += 1

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
