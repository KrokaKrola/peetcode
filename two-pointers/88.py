def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    result = []
    p1 = p2 = 0

    while p1 < m and p2 < n:
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        else:
            result.append(nums2[p2])
            p2 += 1

    for k in range(p1, m):
        result.append(nums1[k])

    for k in range(p2, n):
        result.append(nums2[k])

    for i in range(len(nums1)):
        nums1[i] = result[i]


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
