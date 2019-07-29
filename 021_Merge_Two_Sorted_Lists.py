"""
https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.
"""
__author__ = 'abhireddy96'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Assign dummy node
        head = cur = ListNode(0)

        # Loop till list with minimum elements
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            # Assign Current node
            cur = cur.next

            # Assign remaining list as it is
        cur.next = l1 or l2

        # return next node of head as dummy node was assigned to head
        return head.next


if __name__ == "__main__":
    length = 10
    list1 = [ListNode(2 * i) for i in range(length)]
    list2 = [ListNode(2 * i + 1) for i in range(length)]
    for i in range(length - 1):
        list1[i].next = list1[i + 1]
        list2[i].next = list2[i + 1]

    print(Solution().mergeTwoLists(list1[0], list2[0]))
