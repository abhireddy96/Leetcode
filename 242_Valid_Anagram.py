"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
Note:
You may assume the string contains only lowercase alphabets.
"""
__author__ = 'abhireddy96'


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Make everything lowercase
        # Trim spaces
        # Sort characters
        s = sorted(s.replace(' ', '').lower())
        t = sorted(t.replace(' ', '').lower())
        return 'YES' if s == t else 'NO'


if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
