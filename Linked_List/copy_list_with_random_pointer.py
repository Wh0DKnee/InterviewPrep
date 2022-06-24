
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # idea: use hashmap to map from original node to copied node
        old_to_new = {None: None}
        cur = head
        while cur:
            new_node = Node(cur.val)
            old_to_new[cur] = new_node
            cur = cur.next

        cur = head
        while cur:
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]
