class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]

            if num1 > num2:
                p2 += 1
            elif num1 < num2:
                p1 += 1
            else:
                return num1

        return -1


# print(Solution().getCommon([100, 200, 300], [50, 100, 150, 200]))
print(Solution().getCommon([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))
# print(
#     Solution().getCommon(
#         [5, 15, 16, 20, 22, 39, 43, 44, 44, 55, 61, 62, 62, 64, 72, 73, 81, 88, 90, 95],
#         [2, 8, 9, 11, 12, 13, 26, 29, 38, 49, 50, 51, 58, 63, 67, 72, 75, 82, 92, 96],
#     )
# )
