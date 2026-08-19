class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        print(s)


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))
