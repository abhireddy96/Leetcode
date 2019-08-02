"""
https://leetcode.com/problems/find-pivot-index/
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]):
        # Calculate Total Sum
        total_sum = sum(nums)
        left_sum = 0
        # Iterate from starting index
        for i, v in enumerate(nums):
            # Subtract value from total sum
            total_sum -= v
            if left_sum == total_sum:
                return i
            # Add value to left sum
            left_sum += v
        # equilibrium point not found
        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
