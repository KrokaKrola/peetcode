def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1_idx = m - 1
    nums2_idx = n - 1

    for i in range(len(nums1) - 1, -1, -1):
        if nums2_idx < 0:
            break
        if nums1[nums1_idx] > nums2[nums2_idx]:
            nums1[i] = nums1[nums1_idx]
            nums1_idx -= 1
        else:
            nums1[i] = nums2[nums2_idx]
            nums2_idx -= 1

    if nums2_idx >= 0:
        for i in range(nums2_idx + 1):
            nums1[i] = nums2[i]

    print(nums1)


# merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([1], 1, [], 0)
# merge([0], 0, [1], 1)
merge([2, 0], 1, [1], 1)
