"""
https://leetcode.com/problems/powx-n/
Implement pow(x, n).
"""
__author__ = 'abhireddy96'


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        # Check if radix is 0
        if n == 0:
            return res

        # Remove sign
        i = abs(n)
        # Loop till number is 0
        while i > 0:
            if i & 1 == 1:
                res *= x
            # Bitwise Right shift to perform divide by 2
            i >>= 1
            # Multiply number by itself
            x *= x
        # Check if radix is negative
        # if so, return reciprocate of result
        if n < 0:
            return 1 / res

        return res


if __name__ == "__main__":
    print(Solution().myPow(2.00000, -2))
