class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uppers: dict[str, int] = dict()
        lowers: dict[str, int] = dict()
        result = 0

        for i in range(len(word)):
            if word[i].islower():
                lowers[word[i]] = i
            elif word[i].isupper() and word[i] not in uppers:
                uppers[word[i]] = i

        for key in lowers:
            upper_key = key.upper()
            if upper_key in uppers and lowers[key] < uppers[upper_key]:
                result += 1

        return result


print(Solution().numberOfSpecialChars("aaAbcBC"), 3)
print(Solution().numberOfSpecialChars("abc"), 0)
print(Solution().numberOfSpecialChars("AbBCab"), 0)
