class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0

        depth = 0

        for el in s:
            if el == "(":
                depth += 1
                result = max(result, depth)
            elif el == ")":
                depth -= 1

        return result


print(Solution().maxDepth("((()))"))
print(Solution().maxDepth("()"))
print(Solution().maxDepth("(1 + (2 * (3 + 5)))"))
