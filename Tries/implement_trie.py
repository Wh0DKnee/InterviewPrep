class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root

        i = 0
        for c in word:
            if c not in cur.children:
                break
            cur = cur.children[c]
            i += 1

        for j in range(i, len(word)):
            cur.children[word[j]] = Node()
            cur = cur.children[word[j]]

        cur.isWord = True

    def search(self, word: str) -> bool:
        node = self.getNode(word)
        return node.isWord if node is not None else False

    def startsWith(self, prefix: str) -> bool:
        node = self.getNode(prefix)
        return node is not None

    def getNode(self, s) -> Node:
        cur = self.root

        for c in s:
            if c not in cur.children:
                return None
            cur = cur.children[c]

        return cur

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)