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
        # Start with 1
        res = "1"
        # Iterate n times
        for i in range(1, n):
            res = self.count(res)
        return res

    def count(self, num):
        s = ''
        i = 0
        # Iterate over each digit in number
        while i < len(num):
            j = i + 1
            # Loop till next different digit
            while j < len(num) and num[i] == num[j]:
                j += 1
            # Count of current digit
            count = j - i
            # Resultant String = count of digit + digit itself
            s += str(count) + str(num[i])
            # Assign index of next digit
            i = j
        return s


if __name__ == "__main__":
    print(Solution().countAndSay(4))
