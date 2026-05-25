class Solution:
    parentheses = {"(": ")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        stack = []

        for el in s:
            if el in self.parentheses:
                stack.append(el)
            else:
                if len(stack) == 0 or self.parentheses[stack[-1]] != el:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


print(Solution().isValid("()"), True)
print(Solution().isValid("()[]{}"), True)
print(Solution().isValid("(]"), False)
print(Solution().isValid("([])"), True)
print(Solution().isValid("]]"), False)
print(Solution().isValid("([)])"), False)
print(Solution().isValid("["), False)
