class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest_str_idx = 0
        size = 200

        for idx in range(0, len(strs)):
            el = strs[idx]

            if size > len(el):
                size = len(el)
                smallest_str_idx = idx

        smallest_str = strs[smallest_str_idx]

        for ch_idx in range(0, len(smallest_str)):
            is_common = True
            for curr_str in strs:
                if curr_str[ch_idx] != smallest_str[ch_idx]:
                    is_common = False
                    break

            if not is_common:
                return smallest_str[:ch_idx]

        return smallest_str


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["ab", "a"]))
