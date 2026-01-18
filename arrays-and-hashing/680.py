class Solution:
    def isPalindrome(self, ss: str) -> bool:
        lp = 0
        rp = len(ss) - 1

        while lp < rp:
            if ss[lp] != ss[rp]:
                return False

            lp += 1
            rp -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            if s[lp] != s[rp]:
                return self.isPalindrome(s[lp:rp]) or self.isPalindrome(
                    s[lp + 1 : rp + 1]
                )
            lp += 1
            rp -= 1

        return True


print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome("abc"))
