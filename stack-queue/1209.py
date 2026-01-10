class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for el in s:
            if stack and stack[-1][0] == el:
                stack[-1] = (el, stack[-1][1] + 1)
            else:
                stack.append((el, 1))

            if stack and stack[-1][0] == el and stack[-1][1] >= k:
                stack.pop()

        res = ""

        for el in stack:
            res += el[0] * el[1]

        return res


print(Solution().removeDuplicates("abcd", 2))
print(Solution().removeDuplicates("deeedbbcccbdaa", 3))
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2))
