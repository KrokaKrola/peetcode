class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result = []

        for el in asteroids:
            if el < 0:
                # pop while prev element is positive, and smaller the current element
                while result and result[-1] > 0 and abs(el) > abs(result[-1]):
                    result.pop()

                # if current negative element is equal to prev element
                # => destory both
                if result and result[-1] > 0 and abs(el) == result[-1]:
                    result.pop()
                # if prev element is negative or stack is empty, add to the stack
                elif not result or result[-1] < 0:
                    result.append(el)
            else:
                result.append(el)

        return result


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([3, 5, -6, 2, -1, 4]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))
print(Solution().asteroidCollision([-2, -2, 1, -2]))
print(Solution().asteroidCollision([-2, -2, -1, -2]))
