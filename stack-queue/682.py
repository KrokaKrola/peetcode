class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for el in operations:
            if el == "C":
                record.pop()
            elif el == "D":
                record.append(record[-1] * 2)
            elif el == "+":
                first, second = record[-1], record[-2]
                record.append(first + second)
            else:
                record.append(int(el))

        return sum(record)


print(Solution().calPoints(["5", "2", "C", "D", "+"]))
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(Solution().calPoints(["1", "C"]))
