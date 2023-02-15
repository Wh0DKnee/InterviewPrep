from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(1) space solution
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Here, slow will be the middle for odd lengths
        # and the right middle element for even lengths.

        # Reverse second half of the list, disconnect middle
        # element from first half (by setting next to None),
        # so that the last loop has a clean break condition.
        prev, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # Iterate from left and right until we find a mismatch.
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    # O(n) space solution
    def isPalindrome_linear_space(self, head: Optional[ListNode]) -> bool:
        s = []
        cur = head
        while cur:
            s.append(str(cur.val))
            cur = cur.next
        s = ''.join(s)
        return s == s[::-1]
