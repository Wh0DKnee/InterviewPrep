class TrieNode:

    def __init__(self):
        self.children = {}
        self.val = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, s, val):
        cur = self.root

        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.val = val

    def find(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                return False, None
            cur = cur.children[c]

        return True, cur


class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        exists, node = self.trie.find(prefix)

        if not exists:
            return 0

        def dfs(n):
            children_sum = 0
            for child in n.children.values():
                children_sum += dfs(child)
            return n.val + children_sum

        return dfs(node)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)