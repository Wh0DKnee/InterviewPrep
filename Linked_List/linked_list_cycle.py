from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        cur = head

        while cur:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next

        return False

    # The reason that this works is that once both pointers are in a cycle,
    # the fast pointer is guaranteed to catch up to the slow pointer, because
    # the distance between both shrinks by 1 with each step (the slow pointer
    # moves one forward, the fast pointer two, which means it catches up by 1
    # in each iteration). I was worried that the fast pointer may skip the slow
    # pointer, but that's not possible (would be for 3 jumps though, the fast
    # pointer needs to move with speed 2!).
    def floys_tortoise_and_hare(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
