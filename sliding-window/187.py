from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequences = defaultdict(int)
        left = 0
        right = 10
        result = []

        for right in range(10, len(s) + 1):
            curr_seq = s[left:right]
            sequences[curr_seq] += 1

            if sequences[curr_seq] == 2:
                result.append(curr_seq)

            left += 1

        return result


print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"))
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))
