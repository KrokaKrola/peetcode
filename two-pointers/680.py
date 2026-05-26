class Solution:
    def isPalindrom(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            else:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while lp < rp:
            if s[lp] != s[rp]:
                return self.isPalindrom(s[lp:rp]) or self.isPalindrom(
                    s[lp + 1 : rp + 1]
                )

            lp += 1
            rp -= 1

        return True


# print(Solution().validPalindrome("aba"))
# print(Solution().validPalindrome("abca"))
# print(Solution().validPalindrome("abc"))
print(Solution().validPalindrome("cbbcc"))
