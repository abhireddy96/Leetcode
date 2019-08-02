"""
https://leetcode.com/problems/integer-to-roman/
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ = 'abhireddy96'


class Solution:
    def intToRoman(self, num: int) -> str:
        # Hash map of roman letters with corresponding number
        rom = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC",
               100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        res = ''
        # Iterate over roman letters from highest to lowest
        for i in reversed(list(rom.keys())):

            while num >= i:
                # Append Roman letter to string
                # Subtract corresponding value from number
                res += rom[i]
                num -= i
        return res


if __name__ == "__main__":
    print(Solution().intToRoman(1994))
