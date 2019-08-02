"""
https://leetcode.com/problems/missing-number/
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space
complexity?
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Find sum of n integers using S(n) = n(n+1)/2 formula
        total_sum = len(nums) * (len(nums) + 1) // 2
        # Find sum of array elements
        obtained_sum = sum(nums)
        # Missing number is (sum of n integers) - (sum of array elements)
        return total_sum - obtained_sum


if __name__ == "__main__":
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
