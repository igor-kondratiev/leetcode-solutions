"""Solution for problem https://leetcode.com/problems/intersection-of-two-linked-lists/
The main idea is to truncate longer list from it's head (making both of them having same length)
and then check corresponding items.
In the end we'll get either intersection node (if present) or None if there is no intersection
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    @staticmethod
    def getListLength(head):
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        lenA, lenB = self.getListLength(headA), self.getListLength(headB)
        if lenA > lenB:
            for i in xrange(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for i in xrange(lenB - lenA):
                headB = headB.next

        while headA is not headB:
            headA, headB = headA.next, headB.next

        return headA


if __name__ == '__main__':
    import checker
    a = [ListNode(i) for i in xrange(2)]
    b = [ListNode(i) for i in xrange(3)]
    c = [ListNode(i) for i in xrange(3)]
    headA, headB = a[0], b[0]
    a[0].next = a[1]
    a[1].next = c[0]
    c[0].next = c[1]
    c[1].next = c[2]
    b[0].next = b[1]
    b[1].next = b[2]
    b[2].next = c[0]
    cases = (
        {'args': (headA, headB), 'result': c[0]},
        {'args': (ListNode(0), ListNode(1)), 'result': None},
    )
    checker.check(Solution().getIntersectionNode, cases)
