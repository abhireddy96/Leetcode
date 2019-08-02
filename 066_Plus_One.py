"""
https://leetcode.com/problems/plus-one/
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert list to single number
        n = [str(i) for i in digits]
        # Add one to number
        res = int(''.join(n)) + 1
        # Convert number to list again
        return [int(i) for i in str(res)]


if __name__ == "__main__":
    print(Solution().plusOne([4, 3, 2, 1]))
