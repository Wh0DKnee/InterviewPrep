from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return None
        # TODO: implement recursively

    def reverse_iteratively(self, head):
        cur, prev = head, None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
