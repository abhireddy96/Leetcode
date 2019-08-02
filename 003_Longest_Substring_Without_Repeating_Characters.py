"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""
__author__ = 'abhireddy96'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = []
        # Max number of distinct characters
        m = 0
        # Iterate over string
        for x in s:
            # check if character already present in distinct character list,
            # if so remove all the elements to it's left
            if x in ls:
                ls = ls[ls.index(x) + 1:]
            # Append character to right
            ls.append(x)
            # Check if length of distinct character list is greater than previous best
            m = max(m, len(ls))

        return m


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
