class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []

        for el in logs:
            if stack and el == "../":
                stack.pop()
            elif el != "./" and el != "../":
                stack.append(el)

        return len(stack)


print(Solution().minOperations(["d1/", "d2/", "../", "d21/", "./"]))
print(Solution().minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(Solution().minOperations(["d1/", "../", "../", "../"]))
print(Solution().minOperations(["./", "../", "./"]))
