"""
https://leetcode.com/problems/add-two-numbers/
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
__author__ = 'abhireddy96'


# Node class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Create linked list from number
def create_list(num):
    # Reverse number
    s = str(num)[::-1]
    head = prev = None
    # Iterate over each digit in number
    for ch in s:
        # Create node for each digit
        node = ListNode(int(ch))
        # Assign node prev pointer
        if prev is not None:
            prev.next = node
        prev = node
        # Check if list is empty
        if head is None:
            head = prev
    # Return head pointer
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cnt = 1
        n1 = 0
        n2 = 0
        # Iterate until size of small list
        while l1 is not None and l2 is not None:
            # Compute whole number from linked list
            n1 = n1 + cnt * l1.val
            n2 = n2 + cnt * l2.val
            # Traverse to next node
            l1 = l1.next
            l2 = l2.next
            # Increase count by 10 times
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








