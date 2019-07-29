"""
https://leetcode.com/problems/implement-strstr/
Implement strStr().
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""
__author__ = 'abhireddy96'


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))
