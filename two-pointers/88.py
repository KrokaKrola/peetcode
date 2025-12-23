# merge backwards
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p1 + p2 + 1] = nums1[p1]
            p1 -= 1
        else:
            nums1[p1 + p2 + 1] = nums2[p2]
            p2 -= 1

    if p2 >= 0:
        for i in range(p2 + 1):
            nums1[i] = nums2[i]


# merge from the begining and with helper array
def merge_2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    results = []
    p1 = p2 = 0

    while p1 < m and p2 < n:
        if nums1[p1] < nums2[p2]:
            results.append(nums1[p1])
            p1 += 1
        else:
            results.append(nums2[p2])
            p2 += 1

    for i in range(p1, m):
        results.append(nums1[i])

    for i in range(p2, n):
        results.append(nums2[i])

    for i in range(len(results)):
        nums1[i] = results[i]
    print(nums1)


# merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([1], 1, [], 0)
# merge([0], 0, [1], 1)

merge_2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge_2([1], 1, [], 0)
merge_2([0], 0, [1], 1)
