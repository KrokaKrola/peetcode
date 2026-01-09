class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Stack of waiting day indices; pop and record answer when warmer temp found"""
        result = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures)):
            curr_temp = temperatures[idx]

            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day_idx = stack.pop()
                result[prev_day_idx] = idx - prev_day_idx

            stack.append(idx)

        return result


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([30, 60, 90]))
