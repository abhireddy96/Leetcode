"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""
__author__ = 'abhireddy96'


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Is string is empty
        if not s:
            return s
        # Contains single character
        if len(s) == 1:
            return s

        # Let first character be resultant palindrome
        res = s[0]

        # Iterate over string characters
        for i in range(0, len(s)):

            # Check for Palindrome odd length
            cur = self.palindrome_from_center(s, i, i)
            if len(cur) > len(res):
                res = cur

            # Check for Palindrome even length
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
