class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        result = 0
        left = 0
        sum = 0

        for right in range(len(arr)):
            window_size = right - left + 1
            sum += arr[right]

            if window_size >= k:
                if sum / k >= threshold:
                    result += 1

                sum -= arr[left]
                left += 1

        return result


print(Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
print(Solution().numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
print(Solution().numOfSubarrays([5], 1, 5))
print(Solution().numOfSubarrays([1], 1, 5))
