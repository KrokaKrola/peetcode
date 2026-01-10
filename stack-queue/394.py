class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for el in s:
            if el != "]":
                stack.append(el)
            else:
                str = ""

                while stack and stack[-1] != "[":
                    str = stack.pop() + str

                stack.pop()

                digit = ""

                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append(int(digit) * str)

        return "".join(stack)


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("100[leetcode]"))
