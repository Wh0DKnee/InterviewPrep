from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = ListNode()
        prev = dummy
        carry = 0

        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            added = (val1 + val2 + carry)
            carry = 1 if added > 9 else 0
            new_node = ListNode(added % 10)
            prev.next = new_node
            prev = new_node
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        if carry:
            prev.next = ListNode(1)

        return dummy.next
