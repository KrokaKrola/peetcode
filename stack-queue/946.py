class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        popped_c = 0

        for el in pushed:
            stack.append(el)

            while stack and stack[-1] == popped[popped_c]:
                stack.pop()
                popped_c += 1

        return len(stack) == 0


print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
