class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for el in num:
            while stack and int(stack[-1]) > int(el) and k > 0:
                stack.pop()
                k -= 1

            stack.append(el)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")

        return result if result != "" else "0"


print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("10200", 1))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("9", 1))
print(Solution().removeKdigits("112", 1))
print(Solution().removeKdigits("33526221184202197273", 19))
