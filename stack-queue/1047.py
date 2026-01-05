class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for el in s:
            if stack and stack[-1] == el:
                stack.pop()
            else:
                stack.append(el)

        return "".join(stack)


print(Solution().removeDuplicates("abbaca"))
print(Solution().removeDuplicates("azxxzy"))
