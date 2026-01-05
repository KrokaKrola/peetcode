class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(": ")", "{": "}", "[": "]"}

        for el in s:
            if el in m:
                stack.append(el)
            else:
                if not stack:
                    return False

                prev = stack.pop()
                if m[prev] != el:
                    return False

        return len(stack) == 0


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([])"))
print(Solution().isValid("]]"))
print(Solution().isValid("([)])"))
print(Solution().isValid("["))
