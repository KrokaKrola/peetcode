class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        data: dict[str, list[str]] = {}

        for s in strs:
            c_str = sorted(s)
            c_str = "".join(c_str)

            if c_str not in data:
                data[c_str] = [s]
            else:
                data[c_str].append(s)

        return list(data.values())

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        data = {}

        for s in strs:
            chars = [0] * 28

            for c in s:
                idx = ord(c) - 97
                chars[idx] = chars[idx] + 1

            val = "-".join(str(c) for c in chars)

            if val not in data:
                data[val] = [s]
            else:
                data[val].append(s)

        return list(data.values())


print(Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))

print(Solution().groupAnagrams2(["bdddddddddd", "bbbbbbbbbbc"]))
