import random


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
        def partition(low, high):
            pivot = nums[(low + high) // 2]
            i, j = low - 1, high + 1

            def swap(i, j):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp

            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1

                j -= 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    return j

                swap(i, j)

        def quickSort(low, high):
            if low < high:
                pivot_idx = partition(low, high)
                quickSort(low, pivot_idx)
                quickSort(pivot_idx + 1, high)

        def quickSort2(low, high):
            if low >= high:
                return

            pivot = nums[random.randint(low, high)]
            lt, i, gt = low, low, high  # lt: <pivot boundary, gt: >pivot boundary

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            quickSort2(low, lt - 1)
            quickSort2(gt + 1, high)

        quickSort2(0, len(nums) - 1)

        return nums

    def sortArray_heap(self, nums: list[int]) -> list[int]:
        """"""


print(Solution().sortArray_quick([5, 4, 3, 2, 1]))
