def removeDuplicates(nums: list[int]) -> int:
    i = 1

    tp = 0
    bp = 1

    while tp < len(nums) and bp < len(nums):
        if nums[tp] == nums[bp]:
            bp += 1
        else:
            nums[i] = nums[bp]
            i += 1
            tp = bp
            bp += 1

    return i


def removeDuplicates2(nums: list[int]) -> int:
    j = 0

    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j + 1


print(removeDuplicates2([1, 1, 2]))
print(removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates2([1, 1]))
