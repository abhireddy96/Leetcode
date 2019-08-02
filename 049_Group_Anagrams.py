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

        # Iterate over list of words
        for s in strs:
            # Sort letters in word
            sr = ''.join(sorted(s))
            # check if sorted word is in hash map
            # If so, add current word(unsorted) as it is into hash map as value(i.e hash map value field is list)
            if sr in res:
                res[sr].append(s)
            # If not, add sorted word as key
            # current word(unsorted) as it is into hash map as value(i.e hash map value field is list)
            else:
                res[sr] = [s]
        # return hash map values which contains list of anagrams
        return res.values()


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
