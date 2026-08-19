class Solution:
    parentheses = {"(": ")", "{": "}", "[": "]"}

    def is_valid(self, s: str) -> bool:
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


print(Solution().is_valid("()"), True)
print(Solution().is_valid("()[]{}"), True)
print(Solution().is_valid("(]"), False)
print(Solution().is_valid("([])"), True)
print(Solution().is_valid("]]"), False)
print(Solution().is_valid("([)])"), False)
print(Solution().is_valid("["), False)
