class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        res = [0] * N

        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % N]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    res[i] += code[j % N]

        return res

    def decrypt2(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        res = [0] * N

        left = 0
        cur_sum = 0
        for right in range(N + abs(k)):
            cur_sum += code[right % N]

            if right - left + 1 > abs(k):
                cur_sum -= code[left % N]
                left = (left + 1) % N

            if right - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % N] = cur_sum
                elif k < 0:
                    res[(right + 1) % N] = cur_sum

        return res


print(Solution().decrypt([5, 7, 1, 4], 3))
print(Solution().decrypt([1, 2, 3, 4], 0))
print(Solution().decrypt([2, 4, 9, 3], -2))

print(Solution().decrypt2([5, 7, 1, 4], 3))
print(Solution().decrypt2([1, 2, 3, 4], 0))
print(Solution().decrypt2([2, 4, 9, 3], -2))
