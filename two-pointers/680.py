class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            r -= 1
            l += 1

        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left:right]) or self.isPalindrome(
                    s[left + 1 : right + 1]
                )

            left += 1
            right -= 1

        return True


print(Solution().validPalindrome("aba"), True)
print(Solution().validPalindrome("abca"), True)
print(Solution().validPalindrome("abc"), False)
print(Solution().validPalindrome("cbbcc"), True)
