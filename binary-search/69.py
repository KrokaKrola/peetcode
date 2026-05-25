class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lp, rp = 0, x - 1

        while lp <= rp:
            pivot = (lp + rp) // 2
            squared = pivot * pivot

            if squared > x:
                rp = pivot - 1
            elif squared < x:
                lp = pivot + 1
            else:
                return pivot

        return rp


print(Solution().mySqrt(2), 1)
print(Solution().mySqrt(4), 2)
print(Solution().mySqrt(8), 2)
print(Solution().mySqrt(16), 4)
print(Solution().mySqrt(20), 4)
print(Solution().mySqrt(30), 5)
