"""
https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
__author__ = 'abhireddy96'


class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        ls = []
        for i in s:
            if i in d:
                sym = ls.pop() if ls else ''
                if d[i] != sym:
                    return False
            else:
                ls.append(i)
        return ls == []


if __name__ == "__main__":
    print(Solution().isValid("{[]}"))
