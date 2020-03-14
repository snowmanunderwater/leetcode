# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{self.val}->{self.next}"


def mergeKLists(lists):
    k = len(lists)
    q = PriorityQueue(maxsize=k)
    dummy = ListNode(None)
    curr = dummy
    for list_idx, node in enumerate(lists):
        if node:
            q.put((node.val, list_idx, node))
    while q.qsize() > 0:
        poped = q.get()
        curr.next, list_idx = poped[2], poped[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, list_idx, curr.next))
    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

print(mergeKLists([l1, l2, l3]))
