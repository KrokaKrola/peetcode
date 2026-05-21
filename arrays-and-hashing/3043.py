class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        result = 0

        arr1_prefixes = set()

        for el in arr1:
            while el > 0 and el not in arr1_prefixes:
                arr1_prefixes.add(el)
                el = el // 10

        for el in arr2:
            while el and el not in arr1_prefixes:
                el = el // 10

            if el in arr1_prefixes:
                result = max(result, len(str(el)))

        return result


print(Solution().longestCommonPrefix([1, 10, 100], [1000]))
print(Solution().longestCommonPrefix([1, 10, 25, 255, 254, 100], [1000, 25]))
print(Solution().longestCommonPrefix([1, 2, 3], [4, 4, 4]))
