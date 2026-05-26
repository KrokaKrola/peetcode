class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_chars = set(word)
        result = 0

        for i in range(26):
            low_ch = chr(ord("a") + i)
            upper_ch = chr(ord("A") + i)

            if low_ch in word_chars and upper_ch in word_chars:
                result += 1

        return result


print(Solution().numberOfSpecialChars("aaAbcBC"))
print(Solution().numberOfSpecialChars("abc"))
print(Solution().numberOfSpecialChars("abBCab"))
print(Solution().numberOfSpecialChars("dDDDd"))
