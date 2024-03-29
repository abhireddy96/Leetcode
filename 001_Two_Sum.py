"""
https://leetcode.com/problems/two-sum/
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map with integers as keys and indices as values
        res = dict()
        # Iterate over list of integers
        for i, v in enumerate(nums):
            # Check if target - current value present in hash map
            # If so, return indices
            if target-v in res:
                return [res[target-v], i]
            # Add integer to hash map -> key = integer , value = index
            else:
                res[v] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum([3, 2, 4], 6))
