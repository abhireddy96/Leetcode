"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'abhireddy96'

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Empty string
        if not strs:
            return ''

        # Sort by number of characters in word
        strs.sort(key=len)
        # Consider word with minimum characters
        minChar = strs[0]
        res = ''

        # Iterate over word with minimum characters
        for i in range(len(minChar)):
            # Add one character to prefix at a time
            prefix = minChar[0:i + 1]
            # Check if all words starts with prefix
            if all([s.startswith(prefix) for s in strs]):
                res = prefix
        return res


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
