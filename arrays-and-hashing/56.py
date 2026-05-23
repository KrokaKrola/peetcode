class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        results = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                results.append(prev)
                prev = interval

        results.append(prev)

        return results


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 3], [2, 5], [5, 9], [10, 13], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
print(Solution().merge([[4, 7], [1, 4]]))
print(Solution().merge([[1, 3]]))
