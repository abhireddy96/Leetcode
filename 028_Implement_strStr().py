"""
https://leetcode.com/problems/implement-strstr/
Implement strStr().
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""
__author__ = 'abhireddy96'


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle string is empty
        if not needle:
            return 0
        # if needle is present in haystack , return matching index
        if needle in haystack:
            return haystack.index(needle)
        # needle is not present in haystack
        return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))
