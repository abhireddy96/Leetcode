"""
https://leetcode.com/problems/remove-element/
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
__author__ = 'abhireddy96'

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
