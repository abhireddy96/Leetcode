"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find max element
        m = max(nums)
        # Check if max element is greater than twice the all other elements present in list excluding itself
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1


if __name__ == "__main__":
    print(Solution().dominantIndex([3, 6, 1, 0]))
