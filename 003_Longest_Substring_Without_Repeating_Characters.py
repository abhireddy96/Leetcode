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
        m = 0
        for x in s:
            if x in ls:
                ls = ls[ls.index(x) + 1:]
            ls.append(x)
            m = max(m, len(ls))

        return m


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
