class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest_str_len = 200
        smallest_str_idx = 0

        for i, str in enumerate(strs):
          if len(str) < smallest_str_len:
            smallest_str_idx = i
            smallest_str_len = len(str)

        prefix_len = 0
        smallest_str = strs[smallest_str_idx]

        for i in range(len(smallest_str)):
            for str in strs:
              if str[i] != smallest_str[i]:
                return strs[smallest_str_idx][0:prefix_len]

            prefix_len = prefix_len + 1

        return strs[smallest_str_idx][0:prefix_len]

    def longestCommonPrefix2(self, strs: list[str]) -> str:
      res = ""

      for i in range(len(strs[0])):
        for s in strs:
          if i == len(s) or s[i] != strs[0][i]:
            return res

        res += strs[0][i]

      return res



print(Solution().longestCommonPrefix2(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix2(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix2(["ab", "a"]))
