class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        results = [0] * len(A)
        frequency = [0] * (len(A) + 1)
        count = 0

        for i in range(len(A)):
            frequency[A[i]] += 1
            if frequency[A[i]] == 2:
                count += 1

            frequency[B[i]] += 1
            if frequency[B[i]] == 2:
                count += 1

            results[i] = count

        return results


print(
    Solution().findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]), "=", [0, 2, 3, 4]
)
