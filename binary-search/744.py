class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        lo = -1
        hi = len(letters)

        target_ord = ord(target)

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if ord(letters[mid]) > target_ord:
                hi = mid
            else:
                lo = mid

        if hi == len(letters):
            return letters[0]

        return letters[hi]


print(Solution().nextGreatestLetter(["c", "f", "j"], "a"), "expected c")
print(Solution().nextGreatestLetter(["c", "f", "j"], "c"), "expected f")
print(Solution().nextGreatestLetter(["c", "f", "j"], "j"), "expected c")
print(Solution().nextGreatestLetter(["c", "f", "j"], "d"), "expected f")
print(Solution().nextGreatestLetter(["x", "x", "y", "y"], "z"), "expected x")
