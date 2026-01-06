import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        left = right = 0
        queue = collections.deque()  # index

        while right < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left value from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1

            right += 1

        return output


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
