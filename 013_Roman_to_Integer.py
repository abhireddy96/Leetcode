"""
https://leetcode.com/problems/roman-to-integer/
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ = 'abhireddy96'


class Solution:
    def romanToInt(self, s: str) -> int:
        adds = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        subs = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}
        res = 0
        for c in s:
            res += adds[c]
        for c in subs:
            if c in s:
                res -= subs[c]
        return res


if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))
