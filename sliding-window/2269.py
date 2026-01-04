class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        left = 0

        num_as_str = str(num)

        for right in range(len(num_as_str)):
            window_size = right - left + 1

            if window_size >= k:
                n = int(num_as_str[left : right + 1])

                if n != 0 and num % n == 0:
                    result += 1

                left += 1

        return result


print(Solution().divisorSubstrings(240, 2))
print(Solution().divisorSubstrings(430043, 2))
