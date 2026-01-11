class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        depth = 0

        for el in s:
            if el == "(":
                if depth > 0:
                    result += el
                depth += 1
            elif el == ")":
                depth -= 1
                if depth > 0:
                    result += el

        return result


print(Solution().removeOuterParentheses("(())"))
print(Solution().removeOuterParentheses("((()))"))
print(Solution().removeOuterParentheses("()"))

print(Solution().removeOuterParentheses("()()"))
print(Solution().removeOuterParentheses("(()())"))
print(Solution().removeOuterParentheses("(()())((()))"))
