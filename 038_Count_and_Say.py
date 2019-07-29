"""
https://leetcode.com/problems/count-and-say/
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
"""
__author__ = 'abhireddy96'


class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            res = self.count(res)
        return res

    def count(self, num):
        s = ''
        i = 0
        while i < len(num):
            # find next different number
            j = i + 1
            while j < len(num) and num[i] == num[j]:
                j += 1
            count = j - i
            s += str(count) + str(num[i])
            i = j
        return s


if __name__ == "__main__":
    print(Solution().countAndSay(4))
