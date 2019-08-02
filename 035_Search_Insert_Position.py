"""
https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Iterate over list of integers
        for i, v in enumerate(nums):
            # check if current value is greater or equal to target
            # If so, insert at current index
            if v >= target:
                return i
        # If target is greater than all the elements in list
        return len(nums)


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))
