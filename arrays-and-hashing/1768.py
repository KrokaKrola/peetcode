class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                new_str += word1[i]
            if i < len(word2):
                new_str += word2[i]

        return new_str


print(Solution().mergeAlternately("abc", "pqr"), "apbqcr")
print(Solution().mergeAlternately("ab", "pqrs"), "apbqrs")
print(Solution().mergeAlternately("abcd", "pq"), "apbqcd")
