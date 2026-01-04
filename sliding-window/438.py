from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_dict = defaultdict(int)
        left = 0
        result = []

        for char in p:
            p_dict[char] += 1

        curr_dict = defaultdict(int)

        for right in range(len(s)):
            char = s[right]
            curr_dict[char] += 1

            window_size = right - left + 1

            if window_size >= len(p):
                if curr_dict == p_dict:
                    result.append(left)

                l_char = s[left]
                left += 1
                curr_dict[l_char] -= 1

                if curr_dict[l_char] == 0:
                    del curr_dict[l_char]

        return result


print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("cbdebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))
print(Solution().findAnagrams("a", "b"))
print(Solution().findAnagrams("a", "a"))
print(Solution().findAnagrams("aaaaaa", "aa"))
