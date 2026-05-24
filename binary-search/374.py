x = 0


def guess(n: int) -> int:
    if n > x:
        return -1
    elif n < x:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        lp, rp = 1, n

        while lp <= rp:
            pivot = (lp + rp) // 2
            result = guess(pivot)

            if result == 1:
                lp = pivot + 1
            elif result == -1:
                rp = pivot - 1
            else:
                return pivot

        return -1
