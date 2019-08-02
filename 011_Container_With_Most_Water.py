"""
https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.
Note: You may not slant the container.
"""
__author__ = 'abhireddy96'

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end = len(height) - 1
        max_area = 0
        # Iterate with two pointers,
        # one pointer from starting index towards right
        # other pointer from from last index towards left
        while beg < end:
            # Compute Max Area
            max_area = max(max_area, (end - beg) * min(height[beg], height[end]))
            # Check if beg pointer height is less than end pointer height
            # If so, increment beg and move to right
            if height[beg] < height[end]:
                beg += 1
            # If not, decrement end and move to left
            else:
                end -= 1

        return max_area


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
