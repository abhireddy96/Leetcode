"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'abhireddy96'

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strs.sort(key=len)
        minChar = strs[0]
        c = ''

        for i in range(len(minChar)):
            ch = minChar[0:i + 1]
            if all([s.startswith(ch) for s in strs]):
                c = ch
        return c


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
