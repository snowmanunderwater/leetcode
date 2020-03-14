# Add Two numbers
# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{self.val}->{self.next}"


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    res = n = ListNode(0)
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry, val = divmod(carry, 10)
        n.next = n = ListNode(val)
    return res.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
