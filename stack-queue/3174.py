class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for el in s:
            if stack and el.isdigit():
                stack.pop()
            else:
                stack.append(el)

        return "".join(stack)


print(Solution().clearDigits("abc"))
print(Solution().clearDigits("cb34"))
