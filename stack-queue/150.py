class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(token))

        return stack[0]


# print(Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)
# print(Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)
print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ),
    22,
)
