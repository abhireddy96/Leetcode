"""
https://leetcode.com/problems/powx-n/
Implement pow(x, n).
"""
__author__ = 'abhireddy96'


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0:
            return res

        i = abs(n)
        while i > 0:
            if i & 1 == 1:
                res *= x
            i >>= 1
            x *= x
        if n < 0:
            return 1 / res
        return res


if __name__ == "__main__":
    print(Solution().myPow(2.00000, -2))
