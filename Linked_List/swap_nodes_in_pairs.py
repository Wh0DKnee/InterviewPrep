from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        one = head

        while one and one.next:
            two = one.next
            prev.next = two
            one.next = two.next
            two.next = one
            prev = one
            one = one.next

        return dummy.next
