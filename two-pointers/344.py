class Solution:
    def reverseString(self, s: list[str]) -> None:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1

        print(s)


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))
