"""
https://leetcode.com/problems/reverse-integer/
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""
__author__ = 'abhireddy96'


class Solution:
    def reverse(self, x: int) -> int:
        # Check if not negative
        if x > 0:
            pos = 1
        else:
            pos = -1

        # Remove sign
        x = abs(x)
        res = 0
        # Iterate till integer is zero
        while x != 0:
            # fetch last digit by performing modulo by 10
            res = res * 10 + x % 10
            # Remove last digit by dividing by 10
            x = x // 10
        # Check if for Integer overflow as per problem constraints
        if res >= 2 ** 31 - 1 or res <= -2 ** 31:
            return 0
        # Return along with sign
        else:
            return int(res * pos)


if __name__ == "__main__":
    print(Solution().reverse(123))
