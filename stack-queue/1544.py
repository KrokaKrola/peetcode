class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []

        for idx in range(len(s)):
            el = s[idx]

            if stack and el == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(el)

        return "".join(stack)


print(Solution().makeGood("leEeetcode"))
print(Solution().makeGood("abBAcC"))
print(Solution().makeGood("s"))
