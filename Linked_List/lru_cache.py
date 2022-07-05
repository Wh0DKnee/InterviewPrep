class Node:

    def __init__(self, key, val):
        self.prev, self.next = None, None
        self.key, self.val = key, val


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_node = {}
        # left and right dummy nodes to avoid edge cases
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def add(self, node):
        l, r = self.right.prev, self.right
        l.next = node
        r.prev = node
        node.prev = l
        node.next = r

    def remove(self, node):
        l, r = node.prev, node.next
        l.next, r.prev = r, l

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.add(node)
            node.val = value
        else:
            node = Node(key, value)
            self.add(node)
            self.key_to_node[key] = node
            if len(self.key_to_node) > self.cap:
                to_remove = self.left.next
                self.remove(to_remove)
                self.key_to_node.pop(to_remove.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
