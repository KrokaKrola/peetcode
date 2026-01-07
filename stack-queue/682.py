class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for el in operations:
            if el == "D":
                new_el = stack[-1] * 2
                stack.append(new_el)
            elif el == "C":
                stack.pop()
            elif el == "+":
                new_el = stack[-1] + stack[-2]
                stack.append(new_el)
            else:
                stack.append(int(el))

        return sum(stack)


print(Solution().calPoints(["5", "2", "C", "D", "+"]))
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(Solution().calPoints(["1", "C"]))
