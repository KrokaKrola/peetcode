class Solution:
    def sortArray_merge(self, nums: list[int]) -> list[int]:
        def merge(arr, left, middle, right):
            leftHalf, rightHalf = arr[left : middle + 1], arr[middle + 1 : right + 1]
            i, j, k = left, 0, 0

            while j < len(leftHalf) and k < len(rightHalf):
                if leftHalf[j] <= rightHalf[k]:
                    arr[i] = leftHalf[j]
                    j += 1
                else:
                    arr[i] = rightHalf[k]
                    k += 1

                i += 1

            while j < len(leftHalf):
                nums[i] = leftHalf[j]
                j += 1
                i += 1

            while k < len(rightHalf):
                nums[i] = rightHalf[k]
                k += 1
                i += 1

        def mergeSort(arr, left, right) -> list[int]:
            if left == right:
                return arr

            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            merge(arr, left, mid, right)

        mergeSort(nums, 0, len(nums) - 1)

        return nums

    def sortArray_quick(self, nums: list[int]) -> list[int]:
        """"""

    def sortArray_heap(self, nums: list[int]) -> list[int]:
        """"""


print(Solution().sortArray_merge([5, 4, 3, 2, 1]))
