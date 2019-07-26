"""
https://leetcode.com/problems/add-two-numbers/
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
__author__ = 'abhireddy96'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(num):
    s = str(num)[::-1]
    head = prev = None
    for ch in s:
        node = ListNode(int(ch))
        if prev is not None:
            prev.next = node
        prev = node
        if head is None:
            head = prev
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cnt = 1
        n1 = 0
        n2 = 0
        while l1 is not None and l2 is not None:
            n1 = n1 + cnt * l1.val
            n2 = n2 + cnt * l2.val
            l1 = l1.next
            l2 = l2.next
            cnt = cnt * 10
        return create_list(n1 + n2)


if __name__ == "__main__":
    l1s = [ListNode(1)]
    l2s = [ListNode(9), ListNode(9)]
    for i in range(len(l1s)-1):
        l1s[i].next = l1s[i+1]
    for i in range(len(l2s)-1):
        l2s[i].next = l2s[i+1]
    Solution().addTwoNumbers(l1s[0], l2s[0])








