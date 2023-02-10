class Node:

    def __init__(self, s=None, count=1):
        self.count = count
        if s:
            self.strs = {s}
        else:
            self.strs = set()
        self.prev, self.next = None, None


class AllOne:

    def __init__(self):
        self.str_to_node = {}
        left, right = Node(None, -1), Node(None, -1)
        left.next, right.prev = right, left
        self.head = left
        self.tail = right

    def inc(self, key: str) -> None:
        if key not in self.str_to_node:
            if self.head.next and self.head.next.count == 1:
                self.head.next.strs.add(key)
                self.str_to_node[key] = self.head.next
            else:
                node = Node(key, 1)
                self._insertLeft(node)
                self.str_to_node[key] = node
        else:
            node = self.str_to_node[key]
            l, r = node.prev, node.next
            node.strs.remove(key)
            if r.count == node.count + 1:
                r.strs.add(key)
                self.str_to_node[key] = r
            else:
                new_node = Node(key, node.count + 1)
                self._insertAfter(node, new_node)
                self.str_to_node[key] = new_node

            if len(node.strs) == 0:
                self._removeNode(node)

    def dec(self, key: str) -> None:
        node = self.str_to_node[key]
        l, r = node.prev, node.next
        node.strs.remove(key)

        if l.count == node.count - 1:
            l.strs.add(key)
            self.str_to_node[key] = l
        elif node.count - 1 != 0:
            new_node = Node(key, node.count - 1)
            self.str_to_node[key] = new_node
            self._insertAfter(l, new_node)
        else:  # count is zero
            del self.str_to_node[key]

        if len(node.strs) == 0:
            self._removeNode(node)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        for s in self.tail.prev.strs:
            break
        return s

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        for s in self.head.next.strs:
            break
        return s

    def _insertLeft(self, node):
        self._insertAfter(self.head, node)

    def _removeNode(self, node):
        l, r = node.prev, node.next
        l.next = r
        r.prev = l

    def _insertAfter(self, reference, node):
        l, r = reference, reference.next
        node.prev = l
        node.next = r
        r.prev = node
        l.next = node


obj = AllOne()
obj.inc("hello")
obj.inc("goodbye")
obj.inc("hello")
obj.inc("hello")
print(obj.getMaxKey())
obj.inc("leet")
obj.inc("code")
obj.inc("leet")
obj.dec("hello")
obj.inc("leet")
obj.inc("code")
obj.inc("code")
print(obj.getMaxKey())
print("hi")
