"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""
__author__ = 'abhireddy96'


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return s
        if len(s) == 1:
            return s

        res = s[0]
        for i in range(0, len(s)):

            # odd length
            cur = self.palindrome_from_center(s, i, i)
            if len(cur) > len(res):
                res = cur

            # even length
            cur = self.palindrome_from_center(s, i, i + 1)
            if len(cur) > len(res):
                res = cur

        return res


    def palindrome_from_center(self, s, begin, end):

        while begin >= 0 and end < len(s) and s[begin] == s[end]:
            # move pointers outwards
            begin -= 1
            end += 1
        return s[begin + 1: end]


if __name__ == "__main__":
    assert Solution().longestPalindrome("dfaaabbbaaac") == "aaabbbaaa"
