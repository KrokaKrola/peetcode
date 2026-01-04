class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        vowels = {"a", "e", "i", "o", "u"}
        left = 0
        vowels_count = 0

        for right in range(len(s)):
            if s[right] in vowels:
                vowels_count += 1

            if right - left + 1 >= k:
                result = max(result, vowels_count)

                if result == k:
                    return result

                if s[left] in vowels:
                    vowels_count -= 1

                left += 1

        return result


print(Solution().maxVowels("abciiidef", 3))
print(Solution().maxVowels("aeiou", 2))
print(Solution().maxVowels("leetcode", 3))
