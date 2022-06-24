from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[r - 1].next = None
            nodes[r].next = nodes[l].next
            nodes[l].next = nodes[r]
            l += 1
            r -= 1

    # Alternative solution with O(1) space complexity: Reverse the second half of the list
    # and then merge the first and the second half.
    def reorderList_alternative(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2