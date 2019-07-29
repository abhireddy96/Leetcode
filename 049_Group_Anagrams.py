"""
https://leetcode.com/problems/group-anagrams/
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for s in strs:
            sr = ''.join(sorted(s))
            print(sr)
            if sr in res:
                res[sr].append(s)
            else:
                res[sr] = [s]
        return res.values()


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
