"""
https://leetcode.com/problems/reverse-integer/
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""
__author__ = 'abhireddy96'


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            pos = 1
        else:
            pos = -1
        x = abs(x)
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
        if res >= 2 ** 31 - 1 or res <= -2 ** 31:
            return 0
        else:
            return int(res * pos)


if __name__ == "__main__":
    print(Solution().reverse(123))
