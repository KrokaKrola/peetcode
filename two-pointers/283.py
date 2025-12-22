def moveZeroes(nums: list[int]) -> None:
    p = 0

    for i in range(1, len(nums)):
        if nums[p] != 0:
            p += 1
        if nums[p] == 0 and nums[i] != 0:
            nums[p] = nums[i]
            nums[i] = 0
            p += 1

    print(nums)


def moveZeroes2(nums: list[int]) -> None:
    p = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1


moveZeroes([0, 1, 0, 3, 12])
# moveZeroes([0])
# moveZeroes([1, 0, 1])
