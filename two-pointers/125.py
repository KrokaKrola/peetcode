class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = []

        for c in s:
            if c.isalnum():
                sanitized.append(c.lower())

        l, r = 0, len(sanitized) - 1

        while l < r:
            if sanitized[l] != sanitized[r]:
                return False

            r -= 1
            l += 1

        return True


print(Solution().isPalindrome("race a car"), False)
print(Solution().isPalindrome(" "), True)
print(Solution().isPalindrome("A man, a plan, a canal: Panama"), True)
print(Solution().isPalindrome("0P"), "false")
print(Solution().isPalindrome("a"), "true")
