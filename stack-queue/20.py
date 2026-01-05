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

        if stack:
            return False

        return True


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([])"))
print(Solution().isValid("]]"))
print(Solution().isValid("([)])"))
print(Solution().isValid("["))
