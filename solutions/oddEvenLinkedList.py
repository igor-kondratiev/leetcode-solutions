"""Solution for https://leetcode.com/problems/odd-even-linked-list/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        swap_flag = False
        swap_target = head
        prev_item, item = head, head.next
        while item:
            if swap_flag:
                # Move current item to swap_target
                temp_item = swap_target.next
                swap_target.next = item
                prev_item.next = item.next
                item.next = temp_item
                swap_target = item

                item = prev_item.next
            else:
                item, prev_item = item.next, prev_item.next

            swap_flag = not swap_flag

        return head
