# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(_):
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid

        return hi
