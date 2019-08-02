"""
https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
__author__ = 'abhireddy96'


class Solution:
    def isValid(self, s: str) -> bool:
        # Hash map of closing and opening parenthesis
        d = {')': '(', ']': '[', '}': '{'}
        ls = []
        # Iterate over string
        for i in s:
            # Check if it is closing parenthesis
            if i in d:
                # If so, pop top element from stack
                sym = ls.pop() if ls else ''
                # Compare if parenthesis of same type
                # If not immediately return False
                if d[i] != sym:
                    return False
            # Check if it is opening parenthesis
            # Add it to stack
            else:
                ls.append(i)
        return ls == []


if __name__ == "__main__":
    print(Solution().isValid("{[]}"))
