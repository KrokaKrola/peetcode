class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for el in s:
            if stack and stack[-1] == "A" and el == "B":
                stack.pop()
            elif stack and stack[-1] == "C" and el == "D":
                stack.pop()
            else:
                stack.append(el)

        return len(stack)


print(Solution().minLength("ABFCACDB"))
print(Solution().minLength("ACBBD"))
